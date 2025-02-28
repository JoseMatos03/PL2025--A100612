import ply.lex as lex

tokens = [
    'SELECT',
    'WHERE',
    'VAR',         # Para variáveis do tipo ?s, ?nome, etc.
    'PREFIXNAME',  # Para algo como dbo:MusicalArtist, foaf:name, etc.
    'STRING',      # Para strings entre aspas
    'LANGTAG',     # Para algo como @en
    'DOT',         # O ponto (.)
    'LBRACE',      # {
    'RBRACE',      # }
    'LIMIT',
    'NUMBER',
    'A'            # Para capturar o 'a' (usado em RDF no lugar de rdf:type)
]

t_SELECT = r'select'
t_WHERE  = r'where'
t_LIMIT  = r'LIMIT'

def t_A(t):
    r'a'
    return t

def t_VAR(t):
    r'\?[a-zA-Z_]\w*'
    return t

def t_PREFIXNAME(t):
    r'[a-zA-Z_]\w*:[a-zA-Z_]\w*'
    return t

def t_STRING(t):
    r'\"[^"]*\"'
    return t

def t_LANGTAG(t):
    r'@[a-zA-Z0-9_-]+'
    return t

t_DOT = r'\.'
t_LBRACE = r'\{'
t_RBRACE = r'\}'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_COMMENT(t):
    r'\#[^\n]*'
    pass

# Ignorar espaços em branco e tabulações
t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caracter inválido: {t.value[0]!r} na linha {t.lexer.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()

if __name__ == "__main__":
    data = """
    # DBPedia: obras de Chuck Berry
    select ?nome ?desc where {
        ?s a dbo:MusicalArtist.
        ?s foaf:name "Chuck Berry"@en .
        ?w dbo:artist ?s.
        ?w foaf:name ?nome.
        ?w dbo:abstract ?desc
    } LIMIT 1000
    """

    lexer.input(data)

    for token in lexer:
        print(token)
