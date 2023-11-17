#Parser for adapscript language

import ply.yacc as yacc
from adapscriptlexer import tokens
from Node import*

precedence = (
    ('nonassoc','GE', 'LE', 'EQ', 'NE', 'GT', 'LT', 'OR'),
    ('left', 'ADD', 'SUB'),
    ('left', 'MUL', 'DIV'),
    ('right', 'UNARY')
)


def p_program(p):
    '''program : programStart'''
    p[0] = p[1]

def p_programStart(p):
    '''programStart : FUNC INIT "(" ")" "{" statements "}" '''
    
def p_statements(p):
    '''statements : statement
                | statements statement
                '''
    
                 
def p_statement(p):
    '''statement : function_calls
                | condition
                | function_declarations
                | expression
                | loops
                | RETURN expression
                | PRINT "(" expression ")"
                | assignment
                '''
                
                
def p_function_declarations(p):
        '''function_declarations : function_declaration'''

def p_function_declaration(p):
        '''function_declaration : FUNC IDENTIFIER "(" ")" ":" datatype "{" function_body "}" '''
        

def p_function_body(p):
        '''function_body : statements'''

def p_function_calls(p):
    '''function_calls : IDENTIFIER "(" ")"
                     | IDENTIFIER "(" ")" function_calls
                     | IDENTIFIER "(" parameters ")" 
                     | IDENTIFIER "(" parameters ")" function_calls'''
                     
def p_parameters(p):
    '''parameters : parameterList'''

def p_parameterList(p):
    '''parameterList : parameter
                    | parameter "," parameterList'''

def p_parameter(p):
    '''parameter : datatype IDENTIFIER'''

def p_datatype(p):
        '''datatype : INT
                    | FLOAT
                    | STRING
                    | ADAPT
                    | VOID'''
                    

def p_expression(p):
        '''expression : atoms
                    | paren_expr
                    | binary_expr'''
            
def p_atom(p):
        '''atoms : INT_VALUE
                | FLOAT_VALUE
                | STRING_VALUE
                | variable'''
                
def p_variable(p):
    '''variable : IDENTIFIER '''

def p_paren_expr(p):
        '''paren_expr : "(" expression ")"'''

def p_binary_expr(p):
        '''binary_expr : atoms ADD expression
                    | atoms SUB expression
                    | atoms MUL expression
                    | atoms DIV expression
                    | atoms OR expression
                    | atoms LE expression
                    | atoms GE expression
                    | atoms EQ expression
                    | atoms NE expression
                    | atoms GT expression
                    | atoms LT expression
                    | UNARY atoms
                    | atoms UNARY'''
        p[0] = BinOpNode(p[2], p[1], p[3])
                    
def p_assignment(p):    
        '''assignment : datatype IDENTIFIER EQUAL expression 
                      | datatype IDENTIFIER EQUAL ACCEPT "(" ")" '''

def p_condition(p):
        '''condition : IF expression "{" statements "}"
                    | IF expression "{" statements "}" ELSE "{" statements "}"'''

def p_loops(p):
        '''loops : loop
                | loop loops'''
        

def p_loop(p):
        '''loop : forLoop
                | whileLoop'''
        

def p_forLoop(p):
        '''forLoop : FOR "(" expression ";" condition ";" expression ")" "{" statements "}"'''
    
def p_whileLoop(p):
        '''whileLoop : WHILE "(" condition ")" "{" statements "}"'''

def p_error(p):
    print(f"Syntax error at line {p.lineno}, position {p.lexpos}: Unexpected token '{p.value}'")
   
   

parser = yacc.yacc( debug=True)
try:
    input = open("input3.txt", "r") 
except EOFError:
    print("End of file Error")
result = parser.parse(input.read())



if result is not None:
        print(result)    
    
    
    
