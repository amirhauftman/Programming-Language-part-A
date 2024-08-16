class ParserError(Exception):
    pass

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_token = self.tokens[self.pos]

    def advance(self):
        self.pos += 1
        self.current_token = self.tokens[self.pos] if self.pos < len(self.tokens) else ('EOF', None)

    def parse(self):
        return self.parse_expression()

    def parse_expression(self):
        if self.current_token[0] == 'NUMBER':
            value = self.current_token[1]
            self.advance()
            return ('NUMBER', value)
        elif self.current_token[1] in '+-*/':
            op = self.current_token[1]
            self.advance()
            left = self.parse_expression()
            right = self.parse_expression()
            return (op, left, right)
        else:
            raise ParserError(f'Unexpected token {self.current_token}')

