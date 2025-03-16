import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'MULT'
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_MULT = r'x'

t_ignore = ' \t'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print("Carácter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

# Definir precedência dos operadores
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULT'),
)

# Regras da gramática
def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_mult(p):
    'term : term MULT factor'
    p[0] = p[1] * p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_number(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_error(p):
    print("Erro de sintaxe:", p)

parser = yacc.yacc()

def parse_expression(expression):
    return parser.parse(expression)

if __name__ == '__main__':
    # Testes da aula
    exp1 = "2+3x2"
    exp2 = "2x7-5x3"

    result1 = parse_expression(exp1)
    result2 = parse_expression(exp2)

    print(f"{exp1} = {result1}")
    print(f"{exp2} = {result2}")

    # Loop interativo
    while True:
        try:
            s = input('expr > ')
        except EOFError:
            break
        if not s:
            continue
        result = parse_expression(s)
        print(result)
