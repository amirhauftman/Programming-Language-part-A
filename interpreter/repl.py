from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

class REPL:
    def __init__(self):
        self.interpreter = Interpreter(('Program', []))

    def run(self):
        while True:
            try:
                user_input = input("λ> ")
                if user_input.lower() in ("exit", "quit"):
                    break
                result = self.execute(user_input)
                print(result)
            except Exception as e:
                print(f"Error: {e}")

    def execute(self, source_code):
        lexer = Lexer(source_code)
        tokens = lexer.get_tokens()
        parser = Parser(tokens)
        ast = parser.parse()
        return self.interpreter.interpret(ast)

    def execute_file(self, filename):
        with open(filename, 'r') as file:
            source_code = file.read()
        return self.execute(source_code)

if __name__ == "__main__":
    repl = REPL()
    repl.run()