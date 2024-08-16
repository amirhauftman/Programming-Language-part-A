import sys
from interpreter.lexer import Lexer, LexerError
from interpreter.parser import Parser, ParserError
from interpreter.interpreter import Interpreter, InterpreterError

def main(filename):
    try:
        with open(filename, 'r') as file:
            source_code = file.read()

        lexer = Lexer(source_code)
        tokens = lexer.get_tokens()
        
        parser = Parser(tokens)
        ast = parser.parse()
        
        interpreter = Interpreter(ast)
        result = interpreter.evaluate()
        
        print(f"Result: {result}")
    except (LexerError, ParserError, InterpreterError) as e:
        print(f"Error: {e}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <filename.lambda>")
        sys.exit(1)
    
    filename = sys.argv[1]
    main(filename)