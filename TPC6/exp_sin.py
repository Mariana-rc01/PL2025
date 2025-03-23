import sys
from exp_lex import lexer

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_token = self.tokens[self.pos] if self.tokens else None

    def skip(self, token_type):
        if self.current_token and self.current_token.type == token_type:
            self.pos += 1
            if self.pos < len(self.tokens):
                self.current_token = self.tokens[self.pos]
            else:
                self.current_token = None
        else:
            raise SyntaxError(f"Expected {token_type}, but found {getattr(self.current_token, 'type', 'EOF')}")

    def parse(self):
        return self.parse_Exp1()

    # Exp1 → Exp2 Exp11
    def parse_Exp1(self):
        left = self.parse_Exp2()
        return self.parse_Exp11(left)

    # Exp11 → ADD Exp1 | SUB Exp1 | ε
    def parse_Exp11(self, left):
        if self.current_token and self.current_token.type in ('ADD', 'SUB'):
            op = self.current_token.type
            self.skip(op)
            right_term = self.parse_Exp2()
            new_left = left + right_term if op == 'ADD' else left - right_term
            return self.parse_Exp11(new_left)
        else:
            return left

    # Exp2 → Exp3 Exp22
    def parse_Exp2(self):
        left = self.parse_Exp3()
        return self.parse_Exp22(left)

    # Exp22 → MUL Exp2 | DIV Exp2 | ε
    def parse_Exp22(self, left):
        if self.current_token and self.current_token.type in ('MUL', 'DIV'):
            op = self.current_token.type
            self.skip(op)
            right_factor = self.parse_Exp3()
            new_left = left * right_factor if op == 'MUL' else left / right_factor
            return self.parse_Exp22(new_left)
        else:
            return left

    # Exp3 → PO Exp1 PC | NUM
    def parse_Exp3(self):
        if self.current_token.type == 'PO':
            self.skip('PO')
            value = self.parse_Exp1()
            self.skip('PC')
            return value
        elif self.current_token.type == 'NUM':
            value = self.current_token.value
            self.skip('NUM')
            return value
        else:
            raise SyntaxError(f"Unexpected token: {self.current_token.type}")

def main():
    for line in sys.stdin:
        if not line:
            continue
        lexer.input(line)
        tokens = list(lexer)
        parser = Parser(tokens)
        try:
            result = parser.parse()
            print(f"Result: {result}\n")
        except SyntaxError as e:
            print(f"Sintaxe error: {e}\n")
        except ZeroDivisionError as e:
            print(f"Error: {e}\n")

if __name__ == "__main__":
    main()