import ply.yacc as yacc
import sys
from exp_lex import tokens

def p_global(p):
    """
    S : ExpI
    """
    print("Expression value: ", p[1])

def p_expI_add(p):
    """
    ExpI : ExpI ADD ExpS
    """
    p[0] = p[1] + p[3]

def p_expI_sub(p):
    """
    ExpI : ExpI SUB ExpS
    """
    p[0] = p[1] - p[3]

def p_expI_expS(p):
    """
    ExpI   : ExpS
    """
    p[0] = p[1]

def p_expS_mul(p):
    """
    ExpS : ExpS MUL Termo
    """
    p[0] = p[1] * p[3]

def p_expS_div(p):
    """
    ExpS : ExpS DIV Termo
    """
    p[0] = p[1] / p[3]

def p_expS_termo(p):
    """
    ExpS   : Termo
    """
    p[0] = p[1]

def p_termo(p):
    """
    Termo : NUM
    """
    p[0] = p[1]

def p_error(p):
    print("Erro sintático",p)
    parser.success = False

# Build the parser
parser = yacc.yacc()

# Read line from input and parse it
for line in sys.stdin:
    parser.success = True
    parser.parse(line)
    if parser.success:
        print("Valid quote: ", line)
    else:
        print("Invalid sentence. Fix it and try again")