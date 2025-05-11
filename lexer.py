# This module defines the lexical analyzer (lexer) using PLY.
# It breaks the input string into tokens (e.g., numbers, operators, identifiers).

import ply.lex as lex

# List of all token types our language understands
tokens = (
    'NUMBER', 'ID',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'EQUALS',
    'LPAREN', 'RPAREN',
    'AND', 'OR', 'NOT',
    'TRUE', 'FALSE'
)

# Regular expressions for simple token types
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_EQUALS  = r'='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_ignore  = ' \t'  # Ignore whitespace and tabs

# Reserved words like 'and', 'or', 'not'
reserved = {
    'and': 'AND',
    'or': 'OR',
    'not': 'NOT',
    'True': 'TRUE',
    'False': 'FALSE'
}

# Match variable names and reserved keywords
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t

# Match integer numbers
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Track line numbers (for future error handling)
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Handle unexpected characters
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
