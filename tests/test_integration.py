import unittest
import os
from interpreter.lexer import Lexer
from interpreter.parser import Parser
from interpreter.interpreter import Interpreter

class TestIntegration(unittest.TestCase):
    def run_lambda_file(self, filename):
        examples_dir = os.path.join(os.path.dirname(__file__), '..', 'examples')
        file_path = os.path.join(examples_dir, filename)
        
        with open(file_path, 'r') as file:
            source_code = file.read()
        
        lexer = Lexer(source_code)
        tokens = lexer.get_tokens()
        parser = Parser(tokens)
        ast = parser.parse()
        interpreter = Interpreter(ast)
        return interpreter.evaluate()

    def test_factorial(self):
        result = self.run_lambda_file('factorial.lambda')
        self.assertEqual(result, 120)  # Assuming factorial(5) is the last expression

    def test_fibonacci(self):
        result = self.run_lambda_file('fibonacci.lambda')
        self.assertEqual(result, 55)  # Assuming fib(10) is the last expression

    def test_arithmetic(self):
        result = self.run_lambda_file('arithmetic.lambda')
        self.assertEqual(result, 15)  # Assuming (3 + 4) * 2 + 1 is the last expression

if __name__ == '__main__':
    unittest.main()