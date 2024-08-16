# Functional Programming Language Interpreter

## Overview
This project is an interpreter for a simple functional programming language that emphasizes function definitions and lambda expressions, without variable assignments or mutable state.

# Lambda Interpreter

This project implements an interpreter for a simple functional programming language. The language supports basic arithmetic operations, boolean logic, comparisons, function definitions, and lambda expressions.

## Project Structure

- `interpreter/`: Main package containing the interpreter components
  - `lexer.py`: Tokenizes input source code
  - `parser.py`: Parses tokens into an Abstract Syntax Tree (AST)
  - `interpreter.py`: Evaluates the AST
  - `repl.py`: Implements a Read-Eval-Print Loop for interactive use
- `tests/`: Contains unit tests for each component
- `main.py`: Entry point for running the interpreter
- `grammar.bnf`: Formal grammar definition of the language
- `syntax.md`: Detailed description of language syntax and features

## Installation

1. Clone this repository:

## Installation
1. Clone the repository:
    ```
    git clone <repository-url>
    cd <repository-directory>
    ```
2. Ensure you have Python installed (version 3.6 or later).

## Usage
### Running a Program
To run a program from a file:

To run a Lambda program:
python main.py <filename.lambda>
Copy
To start the interactive REPL:
python -m interpreter.repl
Copy
## Running Tests

To run all tests:
python -m unittest discover -s tests