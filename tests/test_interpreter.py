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

    # Add other test cases as needed

if __name__ == '__main__':
    unittest.main()
