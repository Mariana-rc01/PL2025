import sys
import re

def tokenize(input_string):

    token_specification = [
        ('SELECT'  , r'\bselect\b'),
        ('WHERE'   , r'\bwhere\b'),
        ('LIMIT'   , r'\bLIMIT\b'),
        ('NUM'     , r'\b\d+\b'),
        ('VARIABLE', r'\?[a-z|A-Z]+'), # ?nome
        ('NAME'    , r'([a-zA-Z0-9_]+:)?[a-zA-Z0-9_]+'), # foaf:name
        ('DOT'     , r'\.'),
        ('TAG'     , r'@\w+'), # @en
        ('STRING'  , r'"[^"]*"'), # "Chuck Berry"
        ('POPEN'   , r'{'), # {
        ('PCLOSE'  , r'}'), # }
        ('COMMENT' , r'^#(.*)'),
        ('NEWLINE' , r'\n'),
        ('SKIP'    , r'[ \t]+'),
        ('ERROR'   , r'.')
    ]

    tok_regex = '|'.join([f'(?P<{id}>{expreg})' for (id, expreg) in token_specification])
    recognized = []
    line = 1
    mo = re.finditer(tok_regex, input_string)

    for m in mo:
        dic = m.groupdict()
        if dic['NEWLINE']:
            line += 1
        elif dic['SELECT']:
            t = ("SELECT", dic['SELECT'], line, m.span())
        elif dic['WHERE']:
            t = ("WHERE", dic['WHERE'], line, m.span())
        elif dic['LIMIT']:
            t = ("LIMIT", dic['LIMIT'], line, m.span())
        elif dic['NUM']:
            t = ("NUM", int(dic['NUM']), line, m.span())
        elif dic['VARIABLE']:
            t = ("VARIABLE", dic['VARIABLE'], line, m.span())
        elif dic['NAME']:
            t = ("NAME", dic['NAME'], line, m.span())
        elif dic['DOT']:
            t = ("DOT", dic['DOT'], line, m.span())
        elif dic['TAG']:
            t = ("TAG", dic['TAG'], line, m.span())
        elif dic['STRING']:
            t = ("STRING", dic['STRING'], line, m.span())
        elif dic['POPEN']:
            t = ("POPEN", dic['POPEN'], line, m.span())
        elif dic['PCLOSE']:
            t = ("PCLOSE", dic['PCLOSE'], line, m.span())
        elif dic['COMMENT']:
            t = ("COMMENT", dic['COMMENT'], line, m.span())
        elif dic['SKIP']:
            continue
        else:
            t = ("ERROR", m.group(), line, m.span())

        if not dic['SKIP'] and not dic['NEWLINE']:
            recognized.append(t)

    return recognized

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 query_lex.py <ficheiro.sparql>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as f:
            code = f.read()
    except FileNotFoundError:
        print(f"Error: '{filename}' wasn't found.")
        sys.exit(1)

    tokens = tokenize(code)
    with open("resolution1.txt", "w") as f:
        for tok in tokens:
            print(tok)
            f.write(f"{tok}\n")

if __name__ == '__main__':
    main()