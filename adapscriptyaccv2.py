import ply.yacc as yacc
import math
from adapscriptlexer import tokens

precedence = (
    ('left','ADD','SUB'),
    ('left','MUL','DIV'),
    ('right','UMINUS'),
)

symbol_table = {}
start= 'statement'
# start='program'

# def p_program(p):
#     '''program : FUNC INIT LPAREN RPAREN "{" statement "}"'''
#     p[0] = p[6]
 
def p_statement_assign(p):
    '''
    statement : IDENTIFIER EQUAL expression
    '''
    symbol_table[p[1]] = p[3]

def p_statement_expression(p):
    '''
    statement : expression
    '''
    print(p[1])

def p_expression_binop(p):
    '''
    expression : expression ADD expression
               | expression SUB expression
               | expression DIV expression
               | expression MUL expression
    '''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]

def p_expression_uminus(p):
    '''
    expression : SUB expression %prec UMINUS
    '''
    p[0] = -p[2]

def p_expression_group(p):
    '''
    expression : LPAREN expression RPAREN
    '''
    p[0] = p[2]

def p_expressions(p):
    '''
    expressions : expressions "," expression
               | 
            
    '''
    if len(p) == 0:
        p[0]=None
        return
    p[0] = [p[1]] if len(p) == 2 else p[1] + [p[3]]

def p_expression_function(t):
    '''
    expression : IDENTIFIER LPAREN expressions RPAREN
    '''
    if t[1] == 'sin':
        if len(t[3]) == 1:
            t[0]=math.sin(float(t[3][0]))
        else:
            print('%s() function need one arguments' % t[1])
        return
    elif t[1] == 'cos':
        if len(t[3]) == 1:
            t[0]=math.cos(float(t[3][0]))
        else:
            print('%s() function need one arguments' % t[1])
        return
    elif t[1] == 'log':
        if len(t[3]) == 1:
            t[0]=math.log(float(t[3][0]))
        else:
            print('%s() function need one arguments' % t[1])
        return
    elif t[1] == 'log10':
        if len(t[3]) == 1:
            t[0]=math.log10(float(t[3][0]))
        else:
            print('%s() function need one arguments' % t[1])
        return
    elif t[1] == 'log2':
        if len(t[3]) == 1:
            t[0]=math.log2(float(t[3][0]))
        else:
            print('%s() function need one arguments' % t[1])
        return
    elif t[1] == 'exp':
        if len(t[3]) == 1:
            t[0]=math.exp(float(t[3][0]))
        else:
            print('%s() function need one arguments' % t[1])
        return
    elif t[1] == 'sqrt':
        if len(t[3]) == 1:
            t[0]=math.sqrt(float(t[3][0]))
        else:
            print('%s() function need one arguments' % t[1])
        return
    elif t[1] == 'acos':
        if len(t[3]) == 1:
            t[0]=math.acos(float(t[3][0]))
        else:
            print('%s() function need one arguments' % t[1])
        return
    elif t[1] == 'atan':
        if len(t[3]) == 1:
            t[0]=math.atan(float(t[3][0]))
        else:
            print('%s() function need one arguments' % t[1])
        return
    elif t[1] == 'radians':
        if len(t[3]) == 1:
            t[0]=math.radians(float(t[3][0]))
        else:
            print('%s() function need one arguments' % t[1])
        return
    elif t[1] == 'sinh':
        if len(t[3]) == 1:
            t[0]=math.sinh(float(t[3][0]))
        else:
            print('%s() function need one arguments' % t[1])
        return
    elif t[1] == 'cosh':
        if len(t[3]) == 1:
            t[0]=math.cosh(float(t[3][0]))
        else:
            print('%s() function need one arguments' % t[1])
        return
    elif t[1] == 'tanh':
        if len(t[3]) == 1:
            t[0]=math.tanh(float(t[3][0]))
        else:
            print('%s() function need one arguments' % t[1])
        return
    elif t[1] == 'asin':
        if len(t[3]) == 1:
            t[0]=math.asin(float(t[3][0]))
        else:
            print('%s() function need one arguments' % t[1])
        return



    elif t[1] == 'ceil':
        if len(t[3]) == 1:
            t[0]=math.ceil(float(t[3][0]))
        else:
            print('%s() function need one arguments' % t[1])
        return
    elif t[1] == 'fabs':
        if len(t[3]) == 1:
            t[0]=math.fabs(float(t[3][0]))
        else:
            print('%s() function need one arguments' % t[1])
        return
    elif t[1] == 'factorial':
        if len(t[3]) == 1:
            t[0]=math.factorial(float(t[3][0]))
        else:
            print('%s() function need one arguments' % t[1])
        return
    elif t[1] == 'floor':
        if len(t[3]) == 1:
            t[0]=math.floor(float(t[3][0]))
        else:
            print('%s() function need one arguments' % t[1])
        return
    elif t[1] == 'copysign':
        if len(t[3]) == 2:
            t[0]=math.copysign(int(t[3][0]), int(t[3][1]))
        else:
            print('%s() function need two arguments' % t[1])
        return
    elif t[1] == 'pow':
        if len(t[3]) == 2:
            t[0]=math.pow(int(t[3][0]), int(t[3][1]))
        else:
            print('%s() function need two arguments' % t[1])
        return
    print('Undefined function \'%s\'' % t[1])
    t[0] = None

def p_expression_number(t):
    '''
    expression : INT_VALUE
               | FLOAT_VALUE
    '''
    t[0] = t[1]

def p_expression_name(t):
    '''
    expression : IDENTIFIER
    '''
    try:
        t[0] = symbol_table[t[1]]
    except LookupError:
        print('Undefined name \'%s\'' % t[1])
        t[0] = None


def p_error(p):
    print(f"Syntax error at line {p.lineno}, position {p.lexpos}: Unexpected token '{p.value}' '{p.type}''")
   

parser = yacc.yacc(debug=0, write_tables=0)
while True:
    try:
        s = input('> ')
    except EOFError:
        break
    parser.parse(s)