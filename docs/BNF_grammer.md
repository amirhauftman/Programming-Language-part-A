<program> ::= <statement> | <statement> <program>
<statement> ::= <function_definition> | <expression>
<function_definition> ::= 'Defun' '{' 'name' ':' <id> ',' 'arguments' ':' '(' <id_list> ')' '}' <expression>
<id_list> ::= <id> | <id> ',' <id_list>
<expression> ::= <arithmetic_expression> | <boolean_expression> | <comparison_expression> | <function_application> | <lambda_expression> | <id> | <number> | <bool>
<arithmetic_expression> ::= <term> | <arithmetic_expression> '+' <term> | <arithmetic_expression> '-' <term>
<term> ::= <factor> | <term> '*' <factor> | <term> '/' <factor> | <term> '%' <factor>
<factor> ::= <number> | '(' <arithmetic_expression> ')'
<boolean_expression> ::= <bool> | <boolean_expression> '&&' <boolean_expression> | <boolean_expression> '||' <boolean_expression> | '!' <boolean_expression>
<comparison_expression> ::= <arithmetic_expression> <comparison_operator> <arithmetic_expression>
<comparison_operator> ::= '==' | '!=' | '<' | '>' | '<=' | '>='
<function_application> ::= <id> '(' <expression_list> ')'
<expression_list> ::= <expression> | <expression> ',' <expression_list>
<lambda_expression> ::= 'Lambd' <id> '.' <expression>
