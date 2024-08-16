# interpreter/__init__.py

"""
Interpreter package initialization.
"""

# Importing main components for easy access
from .lexer import Lexer, LexerError 
from .parser import Parser, ParserError
from .interpreter import Interpreter, InterpreterError
from .repl import REPL

