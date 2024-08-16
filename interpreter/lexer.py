import re

class LexerError(Exception):
    pass

KEYWORDS = {'Defun', 'Lambd', 'True', 'False'}

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]
        self.tokens = []

    def advance(self):
        self.pos += 1
        if self.pos >= len(self.text):
            self.current_char = None  # End of input
        else:
            self.current_char = self.text[self.pos]

    def add_token(self, type, value=None):
        self.tokens.append((type, value))

    def tokenize(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.advance()
            elif self.current_char.isdigit() or (self.current_char == '-' and self.peek().isdigit()):
                self.add_token('NUMBER', self.number())
            elif self.current_char.isalpha() or self.current_char == '_':
                token = self.identifier()
                self.add_token(token[0], token[1])
            elif self.current_char in '+-*/(){}<>':
                self.add_token('OP', self.current_char)
                self.advance()
            elif self.current_char == '&' and self.peek() == '&':
                self.add_token('OP', '&&')
                self.advance()
                self.advance()
            elif self.current_char == '|' and self.peek() == '|':
                self.add_token('OP', '||')
                self.advance()
                self.advance()
            elif self.current_char in ',"':
                self.add_token('PUNCT', self.current_char)
                self.advance()
            else:
                raise LexerError(f'Unexpected character {self.current_char!r} at position {self.pos}')
        self.add_token('EOF', None)

    def number(self):
        result = ''
        is_negative = False
        if self.current_char == '-':
            is_negative = True
            result += self.current_char
            self.advance()
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def identifier(self):
        result = ''
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()
        if result in KEYWORDS:
            return ('KEYWORD', result)
        return ('ID', result)


    def peek(self):
        peek_pos = self.pos + 1
        if peek_pos >= len(self.text):
            return None
        return self.text[peek_pos]

    def get_tokens(self):
        self.tokenize()
        return self.tokens
