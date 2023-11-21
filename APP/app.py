from flask import Flask, request, jsonify
import ply.yacc as yacc
import math
from adapscriptlexer import tokens
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)
    
precedence = (
    ('left', 'ADD', 'SUB'),
    ('left', 'MUL', 'DIV'),
    ('right', 'UMINUS'),
)

symbol_table = {}

start='program'

def p_program(p):
    '''program : FUNC INIT LPAREN RPAREN "{" statements "}"'''
    p[0] = p[6]

def p_statements_group(p):
    '''
    statements : statements statement
               | statement
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]
 
def p_statement_assign(p):
    '''
    statement : IDENTIFIER EQUAL expression
              | IDENTIFIER EQUAL ACCEPT LPAREN RPAREN
              | INT IDENTIFIER EQUAL expression
              | FLOAT IDENTIFIER EQUAL expression
              | STR IDENTIFIER EQUAL expression
              | ADAPT IDENTIFIER EQUAL expression
    '''
    if len(p) == 4:
        # Assuming that the datatype is known or default
        if p[1] in symbol_table:
            print('Variable \'%s\' already defined' % p[1])
        else:
            symbol_table[p[1]] = {'datatype': 'adapt', 'value': p[3]}
            p[0] = f'Variable \'{p[1]}\' defined with value: {p[3]}'
    elif len(p) == 5 and p[2] != 'accept':
        if p[1] == type(p[4]).__name__:
            if p[2] in symbol_table:
                print('Variable \'%s\' already defined' % p[2])
            else:
                symbol_table[p[2]] = {'datatype': p[1], 'value': p[4]}
                p[0] = f'Variable \'{p[2]}\' defined with value: {p[4]}'
        else:
            p[0] = f'Cannot assign {type(p[4]).__name__} to {p[1]}'
    elif p[3] == 'accept':
        if p[1] in symbol_table:
            print('Variable \'%s\' already defined' % p[1])
        else:
            p[0] = f'Enter value for \'{p[1]}\': '
            value = input()
            # Check if the input is an integer
            if value.isdigit():
                value = int(value)
            # Check if the input is a float
            elif value.replace('.', '', 1).isdigit() and value.count('.') < 2:
                value = float(value)
            # If not an integer or a float, keep it as a string

            symbol_table[p[1]] = {'datatype': 'adapt', 'value': value}
            p[0] += f'\nVariable \'{p[1]}\' defined with value: {value}'



def p_statement_expression(p):
    '''
    statement : expression
            | PRINT LPAREN expression RPAREN
            | PRINT LPAREN STRING_VALUE RPAREN
    '''
    if len(p) == 2:
        if isinstance(p[1], dict):
            print(p[1]['value'])
        else:
            print(p[1])
    elif len(p) == 5:
        if isinstance(p[3], dict):
            print(p[3]['value'])
        else:
            print(p[3])


def p_expression_binop(p):
    '''
    expression : expression ADD expression
               | expression SUB expression
               | expression DIV expression
               | expression MUL expression
    '''
    # Check if p[1] and p[3] are variables in the symbol table
    if isinstance(p[1], dict):
        p[1] = p[1]['value']
    if isinstance(p[3], dict):
        p[3] = p[3]['value']

    if isinstance(p[1], (int, float)) and isinstance(p[3], (int, float)) or  p[1] == '+':
        if p[2] == '+': 
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]
        elif p[2] == '*':
            p[0] = p[1] * p[3]
        elif p[2] == '/':
            p[0] = p[1] / p[3]
            
    else:
        print('Cannot perform arithmetic operations on non-numeric values')

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


# supports functions with two parameters only
def p_expressions(p):
    '''
    expressions : expressions "," expression
               | expression
               |
    '''
    if len(p) == 0:
        p[0]=None
        return
    p[0] = [p[1]] if len(p) == 2 else p[1] + [p[3]]

def p_expression_function(p):
    '''
    expression : IDENTIFIER LPAREN expressions RPAREN
    '''
    if p[1] == 'print':
        print(*p[3], sep=' ')
        return
    elif p[1] == 'accept':
        symbol_table[p[3][0]] = input()
        return
    elif p[1] == 'pow':
        if len(p[3]) == 2:
            p[0]=math.pow(int(p[3][0]), int(p[3][1]))
        else:
            print('%s() function need two arguments' % p[1])
        return
    print('Undefined function \'%s\'' % p[1])
    p[0] = None

# def p_expression_function_impl(p):
#     '''
#     expression : FN IDENTIFIER LPAREN RPAREN ":" return_type "{" statements "}"
#                 | FN IDENTIFIER LPAREN EXPRESSION RPAREN ":" return_type "{" statements "}"
#     '''
#     if len(p)==10:
#         symbol_table[p[2]] = {'return_type': 'adapt', 'value': p[8]}





def p_expression_value(t):
    '''
    expression : INT_VALUE
               | FLOAT_VALUE
               | STRING_VALUE
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
    raise Exception(f"Syntax error at line {p.lineno}, position {p.lexpos}: Unexpected token '{p.value}'")


@app.route('/execute', methods=['POST'])
def execute_code():
    data = request.get_json()
    code = data['code']

    result, error = execute_adapscript(code)

    if error:
        return jsonify({'error': error})
    else:
        return jsonify({'result': result})


def execute_adapscript(code):
    parser = yacc.yacc(debug=0, write_tables=0)

    try:
        result = parser.parse(code)
        return result, None
    except Exception as e:
        return None, str(e)


if __name__ == '__main__':
    app.run(host='10.0.2.2', port=5000, debug=True)
