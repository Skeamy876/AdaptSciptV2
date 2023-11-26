from flask_cors import CORS 
from flask import Flask, request, jsonify
from compiler.adapscriptlexer import tokens
from compiler.palmInterpreter import PalmInterpreter
import ply.yacc as yacc

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})


precedence = (
    ('left','ADD','SUB'),
    ('left','MUL','DIV'),
    ('right','UMINUS'),
)

symbol_table = {
}


start='program'
def p_program(p):
    '''program : FUNC INIT LPAREN RPAREN "{" statements "}"'''
    p[0] = ('program', p[6])
    
    

def p_statements_group(p):
    '''
    statements : statements statement
               | statement
    '''
    if len(p) == 2:
        p[0] = ('statements',p[1])
        
    else:
        p[0] =('statements',p[1] + (p[2]))
        
        
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
            p[0] = ('assignment',p[1],p[3])
    elif len(p) == 5 and p[2] != 'accept':
        # if p[1]== type(p[4]).__name__:
        #     if p[2] in symbol_table:
        #         print('Variable \'%s\' already defined' % p[2])
        #     else:
        #         symbol_table[p[2]] = {'datatype': p[1], 'value': p[4]}
        #         p[0] = ('assignment',p[2],p[4])
        # else:
        #     print('Cannot assign %s to %s' % (type(p[4]).__name__, p[1]))
        if p[2] in symbol_table:
                print('Variable \'%s\' already defined' % p[2])
        else:
            symbol_table[p[2]] = {'datatype': p[1], 'value': p[4]}
            p[0] = ('assignment',p[2],p[4])

    
    elif p[3] == 'accept':
        if p[1] in symbol_table:
            print('Variable \'%s\' already defined' % p[1])
        else:
            p[0] = input()
            value = p[0]
            # Check if the input is an integer
            if value.isdigit():
                value = int(value)
            # Check if the input is a float
            elif value.replace('.', '', 1).isdigit() and value.count('.') < 2:
                value = float(value)
            # If not an integer or a float, keep it as a string
            symbol_table[p[1]] = {'datatype': 'adapt', 'value': value}
            p[0] = ('assignment',p[1],value)
    



def p_statement_expression(p):
    '''
    statement : expression
            | PRINT LPAREN expression RPAREN
            | PRINT LPAREN STRING_VALUE RPAREN
            | RETURN expression
    '''
    if len(p) == 2:
        if isinstance(p[1], dict):
            p[0] = ('statement',p[1])
        else:
            p[0] = ('statement',p[1])

    elif len(p) == 5:
        if isinstance(p[3], dict):
            p[0] = ('print',p[3])

        else:
            p[0] = ('print',p[3])
    else:
        p[0] = ('return',p[2])


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

    if isinstance(p[1], (int, float)) and isinstance(p[3], (int, float)) or p[2] in ['+','-', '*', '/']:
       p[0]= ('binop',p[1],p[2],p[3])
    else:
        print('Cannot perform arithmetic operations on non-numeric values')
    

def p_expression_uminus(p):
    '''
    expression : SUB expression %prec UMINUS
    '''
    p[0]= ('uminus',p[2])
    

def p_expression_group(p):
    '''
    expression : LPAREN expression RPAREN
    '''
    p[0] = ('group',p[2])
    

def p_expression_condition(p):
    '''
    expression : expression LE expression
               | expression GE expression
               | expression EQ expression
               | expression NE expression
               | expression GT expression
               | expression LT expression
               | expression AND expression
               | expression OR expression
               | expression INCREMENT
               | DECREMENT expression
               
    '''
    if len(p) == 3:
        p[0] = ('increment',p[2]) if p[1] == '++' else ('decrement',p[2])
        return
    

    if isinstance(p[1], dict):
        p[1] = p[1]['value']
    if isinstance(p[3], dict):
        p[3] = p[3]['value']

    #bug=print statement still executed even if condition is false
    if isinstance(p[1], (int, float, tuple)) and isinstance(p[3], (int, float, tuple)):
       p[0]= ('condition',p[1],p[2],p[3])
    else:
        print('Cannot perform logical operations on non-numeric values')
    



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
    p[0] = ('expressions',[p[1]]) if len(p) == 2 else ('expressions',([p[1] + p[3]]))
    

def p_expression_function(p):
    '''
    expression : IDENTIFIER LPAREN expressions RPAREN
    '''
    if p[1] == 'pow':
        if len(p[3]) == 2:
            p[0] =('math-pow',p[3][0], p[3][1])
            
        else:
            print('%s() function need two arguments' % p[1])
        
    elif p[1] in symbol_table:
        if len(p[3]) == 1:
            if symbol_table[p[1]]['return_type'] == symbol_table[p[3][0][1]]['datatype']:
                p[0] = ('function',p[1],p[3])
            else:
                print('Cannot assign %s to %s' % (symbol_table[p[3][0][1]]['datatype'], symbol_table[p[1]]['return_type']))
        else:
            print('%s() function need one argument' % p[1])
    p[0] = None


def p_expression_if_else(p):
    '''
    expression : IF LPAREN expression RPAREN "{" statements "}" ELSE "{" statements "}"
                | IF LPAREN expression RPAREN "{" statements "}"

    '''
    if len(p)==8:
        p[0] = ('if',p[3],p[6])
    else:
        p[0] = ('if-else',p[3],p[6],p[10])
            
def p_expression_func_param(p):
    '''
    expression : INT IDENTIFIER
               | FLOAT IDENTIFIER
               | STR IDENTIFIER
               | ADAPT IDENTIFIER
    '''
    p[0] = ('param',p[1],p[2])            

def p_expression_function_impl(p):
    '''
    expression : FN IDENTIFIER LPAREN RPAREN ":" INT "{" statements "}"
                | FN IDENTIFIER LPAREN RPAREN ":" FLOAT "{" statements "}"
                | FN IDENTIFIER LPAREN RPAREN ":" STR "{" statements "}"
                | FN IDENTIFIER LPAREN RPAREN ":" VOID "{" statements "}"
                | FN IDENTIFIER LPAREN expressions RPAREN ":" INT "{" statements "}"
                | FN IDENTIFIER LPAREN expressions RPAREN ":" FLOAT "{" statements "}"
                | FN IDENTIFIER LPAREN expressions RPAREN ":" STR "{" statements "}"
                | FN IDENTIFIER LPAREN expressions RPAREN ":" VOID "{" statements "}"
    '''
    if len(p)==10:
        if p[2] in symbol_table:
            print('Function \'%s\' already defined' % p[2])
        else:
            symbol_table[p[2]] = {'return_type': p[6], 'value': p[8]}
            p[0] = ('function-impl',p[2],p[6],p[8])
            
    elif len(p)==11:
        if p[2] in symbol_table:
            print('Function \'%s\' already defined' % p[2])
        else:
            symbol_table[p[2]] = {'return_type': p[7], 'value': p[9]}
            p[0] = ('function-impl',p[2],p[7],p[9])
            




def p_expression_value(p):
    '''
    expression : INT_VALUE
               | FLOAT_VALUE
               | STRING_VALUE
    '''
    p[0] = ('value',p[1])    

def p_expression_name(p):
    '''
    expression : IDENTIFIER
    '''
    try:
        p[0] =('identifier',symbol_table[p[1]])
    except LookupError:
        p[0] = ('identifier',None)


def p_expression_forloop(p):
    '''
    expression : FOR LPAREN statement ";" expression ";" expression RPAREN "{" statements "}"
    '''
    p[0] = ('forloop',p[3],p[5],p[7],p[10])
    


def p_expression_whileloop(p):
    '''
    expression : statement WHILE LPAREN expression RPAREN "{" statements "}"
    '''
    p[0] = ('whileloop',p[1],p[4],p[7])

def p_error(p):
    print(f"Syntax error at line {p.lineno}, position {p.lexpos}: Unexpected token '{p.value}'")
    exit(1)




@app.route('/execute', methods=['POST'])
def execute_code():
    data = request.get_json()
    code = data['code']
    result,semantic_result,error = execute_adapscript(code)
    if error:
        return jsonify({'error': error})
    else:
        return jsonify({'result': result,
                        'semantic_result': semantic_result
                        })

def execute_adapscript(code):
    palm = PalmInterpreter()
    parser = yacc.yacc(write_tables=False, debug=False)
    try:  
        result = parser.parse(code)
        return palm.interpret(result),result, None
    except Exception as e:
        return None, str(e)

@app.after_request  
def clear_symbol_table(response):
    symbol_table.clear()
    return response

if __name__ == '__main__':
    app.run(host='10.0.2.2', port=5000, debug=True)