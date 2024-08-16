import unittest
from interpreter.lexer import Lexer, LexerError

class TestLexer(unittest.TestCase):

    def test_numbers(self):
        lexer = Lexer("42 -3 0")
        tokens = lexer.get_tokens()
        expected = [('NUMBER', 42), ('NUMBER', -3), ('NUMBER', 0), ('EOF', None)]
        self.assertEqual(tokens, expected)

    def test_keywords(self):
        lexer = Lexer("Defun Lambd True False")
        tokens = lexer.get_tokens()
        expected = [('KEYWORD', 'Defun'), ('KEYWORD', 'Lambd'), ('KEYWORD', 'True'), ('KEYWORD', 'False'), ('EOF', None)]
        self.assertEqual(tokens, expected)

    def test_identifiers(self):
        lexer = Lexer("foo bar_123")
        tokens = lexer.get_tokens()
        expected = [('ID', 'foo'), ('ID', 'bar_123'), ('EOF', None)]
        self.assertEqual(tokens, expected)

    def test_complex_expression(self):
        lexer = Lexer("(2 + 3) * {4 > 5} && True")
        tokens = lexer.get_tokens()
        expected = [
            ('OP', '('), ('NUMBER', 2), ('OP', '+'), ('NUMBER', 3), ('OP', ')'), ('OP', '*'), 
            ('OP', '{'), ('NUMBER', 4), ('OP', '>'), ('NUMBER', 5), ('OP', '}'), ('OP', '&&'),
            ('KEYWORD', 'True'), ('EOF', None)
        ]
        self.assertEqual(tokens, expected)

    # Add other test cases as needed

if __name__ == '__main__':
    unittest.main()
