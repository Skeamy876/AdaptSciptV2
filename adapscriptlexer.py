# tokenizer for adapScript programming language
import ply.lex as lex


#Snippets from adapScript programming language

# func init() {
#     print("Hello World")
#     num=accept() #must not have a datype
# }


#dictionary of reserved words
reserved = {
    'int':'INT',
    'str':'STR',
    'float':'FLOAT',
    'adapt':'ADAPT',
    'void':'VOID',
    'init':'INIT',
    'return':'RETURN',
    'for':'FOR',
    'if':'IF',
    'while':'WHILE',
    'else':'ELSE',
    'func':'FUNC',
    'print':'PRINT',
    'accept':'ACCEPT',
    'fn':'FN',
}


literals = ['{', '}', '(', ')', ',','"', ';',':'] #list of literals

#token definitions
tokens = ['UNARY', 'ADD', 'SUB', 'DIV', 'MUL', 'OR', 'LE', 'GE', 'EQ', 'NE', 'GT', 'LT', 'AND', 'EQUAL',
    'INT_VALUE', 'FLOAT_VALUE', 'STRING_VALUE', 'IDENTIFIER', 'WHITESPACE', 'COMMENTS', 'UMINUS', 'LPAREN', 'RPAREN'
]+list(reserved.values())


t_UNARY = r'\+\+|--'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
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
t_ignore_WHITESPACE= r'[ \t\r\v\f]'
t_ignore_COMMENTS = r'\/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+\/'


def t_FLOAT_VALUE(t):
    r'[0-9]*\.[0-9]+'
    t.value = float(t.value)
    return t

def t_INT_VALUE(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

def t_STRING_VALUE(t):
     r'\'[^\']*\'|\"[^\"]*\"'
     t.type = reserved.get(t.value,'STRING_VALUE')
     t.value = str(t.value)
     return t   
 
def t_True(t):
    r'true'
    t.value = True
    return t

def t_False(t):
    r'false'
    t.value = False
    return t
    
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

# test lexer sample output
# input = open("input3.txt", "r") 

# lexer.input(input.read()) #read from input sample file
# input.close()

# while True: 
#     tok = lexer.token()
#     if not tok:
#         break
#     print(tok)
