# This module contains the parser rules for MiniLang.
# It uses PLY's yacc to parse and evaluate expressions.

import ply.yacc as yacc

# Dictionary to store variables
variables = {}

# Operator precedence to handle order of operations
precedence = (
    ('left', 'AND', 'OR'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'NOT'),
)

# Rule for assignment (e.g., x = 5)
def p_statement_assign(p):
    'statement : ID EQUALS expression'
    variables[p[1]] = p[3]
    p[0] = f"{p[1]} = {p[3]}"

# Rule to allow expressions without assignment
def p_statement_expr(p):
    'statement : expression'
    p[0] = p[1]

# Arithmetic and logical operations
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression AND expression
                  | expression OR expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]
    elif p[2] == 'and':
        p[0] = p[1] and p[3]
    elif p[2] == 'or':
        p[0] = p[1] or p[3]

# Unary NOT operator
def p_expression_not(p):
    'expression : NOT expression'
    p[0] = not p[2]

# Parentheses for grouping
def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

# Use numbers directly
def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

# True/False values
def p_expression_true_false(p):
    '''expression : TRUE
                  | FALSE'''
    p[0] = True if p[1] == 'True' else False

# Variable usage
def p_expression_id(p):
    'expression : ID'
    if p[1] in variables:
        p[0] = variables[p[1]]
    else:
        print(f"Undefined variable '{p[1]}'")
        p[0] = 0  # Default fallback

# Syntax error handling
def p_error(p):
    print("Syntax error!")

# Build the parser
parser = yacc.YaccError()
