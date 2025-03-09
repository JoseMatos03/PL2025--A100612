import ply.lex as lex
import json
import sys
from datetime import datetime

balance = 0

# Carregar o stock a partir do ficheiro JSON
try:
    with open("stock.json", "r", encoding="utf-8") as f:
        stock = json.load(f)
except FileNotFoundError:
    print("Ficheiro stock.json não encontrado. A iniciar com stock vazio.")
    stock = []

tokens = (
    'LISTAR',
    'MOEDA',
    'SELECIONAR',
    'SAIR',
    'ADICIONAR',
    'COIN',
    'COMMA',
    'PERIOD',
    'CODE',
    'STRING',
    'NUMBER'
)

t_LISTAR     = r'LISTAR'
t_MOEDA      = r'MOEDA'
t_SELECIONAR = r'SELECIONAR'
t_SAIR       = r'SAIR'
t_ADICIONAR  = r'ADICIONAR'
t_COMMA      = r','
t_PERIOD     = r'\.'

def t_COIN(t):
    r'\d+(e|c)'
    return t

def t_CODE(t):
    r'[A-Z]\d{2}'
    return t

def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    t.value = t.value[1:-1]  # remove as aspas
    return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    if '.' in t.value:
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Carácter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

# Função para converter moeda em cêntimos (1e = 100, 20c = 20)
def coin_to_cents(coin_str):
    if coin_str.endswith('e'):
        return int(coin_str[:-1]) * 100
    elif coin_str.endswith('c'):
        return int(coin_str[:-1])
    return 0

# Função para formatar o saldo (ex.: 130 -> "1e30c")
def format_cents(cents):
    euros = cents // 100
    centavos = cents % 100
    result = ""
    if euros > 0:
        result += f"{euros}e"
    if centavos > 0:
        result += f"{centavos}c"
    if result == "":
        result = "0c"
    return result

# Função para calcular o troco
def get_change_coins(cents):
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    change = {}
    for coin in coins:
        count = cents // coin
        if count:
            change[coin] = count
            cents %= coin
    return change

def format_change(change):
    parts = []
    for coin in sorted(change.keys(), reverse=True):
        coin_str = f"{coin}c" if coin < 100 else f"{coin//100}e"
        parts.append(f"{change[coin]}x {coin_str}")
    if len(parts) > 1:
        return ", ".join(parts[:-1]) + " e " + parts[-1]
    elif parts:
        return parts[0]
    else:
        return "0c"

# Função para listar o stock
def listar_stock():
    print("maq:")
    print("cod    | nome                        | quantidade  | preço")
    print("----------------------------------------------------------")
    for item in stock:
        print(f"{item['cod']:<7}| {item['nome']:<28}| {item['quant']:<12}| {item['preco']}")

# Função para processar os comandos
def process_command(command):
    global balance, stock
    lexer.input(command)
    tokens_list = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens_list.append(tok)
    if not tokens_list:
        return

    # Verifica qual é o comando
    tok = tokens_list[0]
    if tok.type == "LISTAR":
        listar_stock()

    elif tok.type == "MOEDA":
        # Os tokens seguintes (tipo COIN) representam as moedas, separadas por vírgulas
        coins = [token.value for token in tokens_list[1:] if token.type == "COIN"]
        total = sum(coin_to_cents(c) for c in coins)
        balance += total
        print("maq: Saldo =", format_cents(balance))

    elif tok.type == "SELECIONAR":
        # Espera um código de produto a seguir
        if len(tokens_list) < 2:
            print("maq: Comando inválido. Produto não especificado.")
            return
        code = tokens_list[1].value
        # Procura o produto no stock
        product = next((item for item in stock if item['cod'] == code), None)
        if product is None:
            print("maq: Produto inexistente.")
            return
        if product['quant'] <= 0:
            print("maq: Produto esgotado.")
            return
        price_cents = int(round(product['preco'] * 100))
        if balance < price_cents:
            print("maq: Saldo insuficiente para satisfazer o seu pedido")
            print(f"maq: Saldo = {format_cents(balance)}; Pedido = {format_cents(price_cents)}")
            return
        # Dispensa o produto
        product['quant'] -= 1
        balance -= price_cents
        print(f"maq: Pode retirar o produto dispensado \"{product['nome']}\"")
        print("maq: Saldo =", format_cents(balance))

    elif tok.type == "ADICIONAR":
        # ADICIONAR <codigo> , <"nome"> , <quant> , <preco> .
        args = [t for t in tokens_list[1:] if t.type != "COMMA" and t.type != "PERIOD"]
        if len(args) < 4:
            print("maq: Comando ADICIONAR inválido. Use: ADICIONAR <codigo> , <\"nome\"> , <quant> , <preco> .")
            return
        code = args[0].value
        name = args[1].value
        quant = args[2].value
        price = args[3].value
        # Verifica se o produto já existe
        existing = next((item for item in stock if item['cod'] == code), None)
        if existing:
            existing['quant'] += quant
            print(f"maq: Produto \"{name}\" atualizado, nova quantidade: {existing['quant']}.")
        else:
            stock.append({"cod": code, "nome": name, "quant": quant, "preco": price})
            print(f"maq: Produto \"{name}\" adicionado com quantidade {quant} e preço {price}.")

    elif tok.type == "SAIR":
        # Ao sair, dispensa o troco se houver saldo
        if balance > 0:
            change = get_change_coins(balance)
            change_str = format_change(change)
            print("maq: Pode retirar o troco:", change_str + ".")
        print("maq: Até à próxima")
        # Guarda o stock atualizado no ficheiro JSON
        try:
            with open("stock.json", "w", encoding="utf-8") as f:
                json.dump(stock, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print("Erro ao guardar o ficheiro JSON:", e)
        sys.exit(0)

    else:
        print("maq: Comando não reconhecido.")

# Função principal para interação
def main():
    print(f"maq: {datetime.today().strftime('%Y-%m-%d')}, Stock carregado, Estado atualizado.")
    print("maq: Bom dia. Estou disponível para atender o seu pedido.")
    while True:
        try:
            command = input(">> ")
            process_command(command)
        except EOFError:
            break

if __name__ == "__main__":
    main()
