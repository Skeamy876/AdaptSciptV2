# tokenizer for adapScript programming language
import ply.lex as lex


reserved = {
    'int' : 'INT',
    'string' : 'STRING',
    'float' : 'FLOAT',
    'adapt' : 'ADAPT',
    'void' : 'VOID',
    'init' : 'INIT',
    'return' : 'RETURN',
    'for' : 'FOR',
    'if' : 'IF',
    'while' : 'WHILE',
    'else' : 'ELSE',
    'true' : 'TRUE',
    'false' : 'FALSE',
    'func' : 'FUNC',
    'print' : 'PRINT',
    'accept' : 'ACCEPT'
}

literals = ['{', '}', '(', ')', ',','"', ';']

tokens = ['UNARY', 'ADD', 'SUB', 'DIV', 'MUL', 'OR', 'LE', 'GE', 'EQ', 'NE', 'GT', 'LT', 'AND', 'EQUAL',
    'INT_VALUE', 'FLOAT_VALUE', 'CHAR_VALUE', 'STRING_VALUE', 'IDENTIFIER', 'WHITESPACE', 'COMMENTS'
]+list(reserved.values())


t_UNARY = r'\+\+|--'
t_ADD = r'\+'
t_SUB = r'-'
t_DIV = r'/'
t_MUL = r'\*'
t_OR = r'\|'
t_LE = r'<='
t_GE = r'>='
t_EQUAL = r'='
t_EQ = r'=='
t_NE = r'!='
t_GT = r'>'
t_LT = r'<'
t_AND = r'&&'



def t_INT_VALUE(t):
    r'[-]?[0-9]+'
    t.value = int(t.value)
    return t

def t_FLOAT_VALUE(t):
    r'[-]?[0-9]*\.?[0-9]+'
    t.value = float(t.value)
    return t

def t_STRING_VALUE(t):
     r'[a-zA-Z]+'
     t.value = str(t.value)
     return t
 
def t_WHITESPACE(t):
    r'[ \t\r\v\f]'
    pass

def t_COMMENTS(t):
    r'\/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+\/'
    pass
    
def t_IDENTIFIER(t):
    r'[a-zA-Z]([a-zA-Z]|[-]?[0-9]+)*'
    t.type = reserved.get(t.value,'IDENTIFIER')    # Check for reserved words
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
#test lexer sample output
input = open("input2.txt", "r") 

lexer.input(input.read()) #read from input sample file


while True: 
    tok = lexer.token()
    if not tok:
        break
    print(tok)

