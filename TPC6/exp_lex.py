import ply.lex as lex

tokens = ['NUM','ADD', 'SUB', 'MUL', 'DIV']

t_ADD = r'\+'
t_SUB = r'\-'
t_MUL = r'\*'
t_DIV = r'\/'

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = " \t\n"

def t_error(t):
    print("Caracter inválido: ", t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

