import unittest
from unittest.mock import patch
from io import StringIO
from interpreter.repl import REPL

class TestREPL(unittest.TestCase):
    @patch('builtins.input', side_effect=['2 + 3', 'exit'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_basic_arithmetic(self, mock_stdout, mock_input):
        repl = REPL()
        repl.run()
        self.assertIn('5', mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['Defun {\'name\': \'square\', \'arguments\': (x,)} (* x x)', 'square(4)', 'exit'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_function_definition_and_call(self, mock_stdout, mock_input):
        repl = REPL()
        repl.run()
        self.assertIn('16', mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['(Lambd {x} (* x x))(3)', 'exit'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_lambda_expression(self, mock_stdout, mock_input):
        repl = REPL()
        repl.run()
        self.assertIn('9', mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['2 + )', 'exit'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_syntax_error(self, mock_stdout, mock_input):
        repl = REPL()
        repl.run()
        self.assertIn('Error', mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['exit'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_exit(self, mock_stdout, mock_input):
        repl = REPL()
        repl.run()
        self.assertIn('Goodbye', mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()