class InterpreterError(Exception):
    pass

class Interpreter:
    def __init__(self, ast):
        self.ast = ast
        self.global_env = {}
        self.call_stack = []

    def interpret(self):
        return self.eval_node(self.ast)

    def eval_node(self, node):
        node_type = node[0]
        if node_type == 'Program':
            return self.eval_program(node[1])
        elif node_type == 'Number':
            return node[1]
        elif node_type == 'Boolean':
            return node[1]
        elif node_type == 'Identifier':
            return self.lookup_identifier(node[1])
        elif node_type == 'FunctionDefinition':
            return self.eval_function_definition(node[1])
        elif node_type == 'LambdaExpression':
            return self.eval_lambda_expression(node[1])
        elif node_type == 'FunctionCall':
            return self.eval_function_call(node[1])
        # Add more cases for other node types

    # Add methods for eval_program, eval_function_definition, 
    # eval_lambda_expression, eval_function_call, and other necessary evaluation methods

    def lookup_identifier(self, name):
        for env in reversed(self.call_stack):
            if name in env:
                return env[name]
        if name in self.global_env:
            return self.global_env[name]
        raise InterpreterError(f"Undefined identifier: {name}")