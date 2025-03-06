import sys
import ply.lex as lex

tokens = [
    'SELECT',
    'WHERE',
    'LIMIT',
    'NUM',
    'VARIABLE',
    'NAME',
    'DOT',
    'TAG',
    'STRING',
    'POPEN',
    'PCLOSE',
    'COMMENT'
]

t_SELECT   = r'select'
t_WHERE    = r'where'
t_LIMIT    = r'LIMIT'
t_VARIABLE = r'\?[a-zA-Z_]+'
t_NAME     = r'([a-zA-Z0-9_]+:)?[a-zA-Z0-9_]+'
t_DOT      = r'\.'
t_TAG      = r'@[a-zA-Z\-]+'
t_STRING   = r'"[^"]*"'
t_POPEN    = r'\{'
t_PCLOSE   = r'\}'
t_COMMENT  = r'\#.*'

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Invalid caracter '{t.value[0]}' in line {t.lexer.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 query_lex.py <file.sparql>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as f:
            code = f.read()
    except FileNotFoundError:
        print(f"Error: '{filename}' wasn't found.")
        sys.exit(1)

    lexer.input(code)

    with open("resolution2.txt", "w") as f:
        for tok in lexer:
            print(tok)
            f.write(f"{tok}\n")

if __name__ == '__main__':
    main()
