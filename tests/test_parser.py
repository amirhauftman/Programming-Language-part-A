import unittest
from interpreter.lexer import Lexer
from interpreter.parser import Parser, ParserError

class TestParser(unittest.TestCase):

    def parse(self, text):
        lexer = Lexer(text)
        tokens = lexer.get_tokens()
        parser = Parser(tokens)
        return parser.parse()

    def test_arithmetic_expression(self):
        ast = self.parse("(2 + 3) * 4")
        expected = ('OP', '*', ('OP', '+', ('NUMBER', 2), ('NUMBER', 3)), ('NUMBER', 4))
        self.assertEqual(ast, expected)

    def test_boolean_expression(self):
        ast = self.parse("(x > 0) && (y < 10)")
        expected = ('OP', '&&', ('OP', '>', ('ID', 'x'), ('NUMBER', 0)), ('OP', '<', ('ID', 'y'), ('NUMBER', 10)))
        self.assertEqual(ast, expected)

    def test_function_application(self):
        ast = self.parse("factorial(5)")
        expected = ('ID', 'factorial', ('NUMBER', 5))
        self.assertEqual(ast, expected)

    def test_function_definition(self):
        ast = self.parse("Defun {'name': 'factorial', 'arguments': (n,)} (n == 0) or (n * factorial(n - 1))")
        expected = ('KEYWORD', 'Defun', {'name': 'factorial', 'arguments': ('n',)}, 
                    ('OP', 'or', ('OP', '==', ('ID', 'n'), ('NUMBER', 0)), 
                    ('OP', '*', ('ID', 'n'), ('ID', 'factorial', ('OP', '-', ('ID', 'n'), ('NUMBER', 1))))))
        self.assertEqual(ast, expected)

    def test_lambda_expression(self):
        ast = self.parse("Lambd {x, y} (x + y)")
        expected = ('KEYWORD', 'Lambd', ('x', 'y'), ('OP', '+', ('ID', 'x'), ('ID', 'y')))
        self.assertEqual(ast, expected)

    def test_nested_expression(self):
        ast = self.parse("(Lambd {x} (x * x))(3 + 2)")
        expected = ('OP', '(', ('KEYWORD', 'Lambd', ('x',), ('OP', '*', ('ID', 'x'), ('ID', 'x'))), 
                    ('OP', '(', ('OP', '+', ('NUMBER', 3), ('NUMBER', 2)),))
        self.assertEqual(ast, expected)

if __name__ == '__main__':
    unittest.main()
