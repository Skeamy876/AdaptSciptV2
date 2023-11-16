#Parser for adapscript language

import ply.yacc as yacc
from adapscriptlexer import tokens

print(tokens)


precedence = (
    ('left', 'ADD', 'SUB'),
    ('left', 'MUL', 'DIV'),
    ('GE', 'LE', 'EQ', 'NE', 'GT', 'LT', 'OR'),
)

def p_programStart(p):
    'programStart : FUNC INIT "(" ")" "{" function_declarations statements "}"'
    

def p_statements(p):
    '''statements : statement "\\n"
                  | statements statement "\\n"'''
    

def p_statement(p):
    '''statement : function_calls
                | condition
                | expression
                | loops
                | RETURN variable'''
    if p[1] == 'return':
        p[0] = p[2]
    else:
        p[0] = p[1]

def p_function_declarations(p):
        '''function_declarations : "\\n"
                                | function_declaration
                                | function_declaration function_declarations'''
        pass

def p_function_declaration(p):
        'function_declaration : FUNC function_name ":" datatype "{" function_body "}"'
        pass

def p_function_body(p):
        'function_body : statements'
        pass

def p_function_calls(p):
    '''function_calls : function_name
                     | function_name parameters'''
    if len(p) == 2:
        p[0] = (p[1], None)
    elif len(p) == 3:
        p[0] = (p[1], p[2])

def p_variable(p):
    'variable : IDENTIFIER "\\n"'
    p[0] = (p[1], p[2])

def p_parameters(p):
    'parameters : parameterList'
    p[0] = p[1]

def p_parameterList(p):
    '''parameterList : parameter
                    | parameter "," parameterList'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_parameter(p):
    'parameter : datatype IDENTIFIER'
    p[0] = (p[1], p[2])

def p_datatype(p):
        '''datatype : INT
                    | FLOAT
                    | STRING
                    | CHAR
                    | ADAPT
                    | VOID'''
        p[0]= p[1]
            
def p_atom(p):
        '''atom : INT_VALUE
                | FLOAT_VALUE
                | CHAR_VALUE
                | STRING_VALUE
                | variable
                | TRUE
                | FALSE'''
        p[0] = p[1]

def p_paren_expr(p):
        'paren_expr : "(" expression ")"'
        pass

def p_binary_expr(p):
        '''binary_expr : variable ADD expression
                    | variable SUB expression
                    | variable MUL expression
                    | variable DIV expression
                    | variable OR expression
                    | variable LE expression
                    | variable GE expression
                    | variable EQ expression
                    | variable NE expression
                    | variable GT expression
                    | variable LT expression'''
        p[0] = (p[2], p[1], p[3])
def p_expression(p):
        '''expression : atom
                    | paren_expr
                    | binary_expr'''
        p[0] = p[1]

def p_condition(p):
        '''condition : IF expression "{" statements "}"
                    | IF expression "{" statements "}" ELSE "{" statements "}"'''
        if len(p) == 5:
        # IF expression "{" statements "}"
            if p[2]:
                # Execute statements if the condition is true
                for statement in p[4]:
                    execute_statement(statement)
        else:
        # IF expression "{" statements "}" ELSE "{" statements "}"
            if p[2]:
                # Execute statements in the true branch
                for statement in p[4]:
                    execute_statement(statement)
            else:
                # Execute statements in the else branch
                for statement in p[8]:
                    execute_statement(statement)

def p_loops(p):
        '''loops : loop
                | loop loops'''
        

def p_loop(p):
        '''loop : forLoop
                | whileLoop'''
        

def p_forLoop(p):
        'forLoop : FOR "(" expression ";" condition ";" expression ")" "{" statements "}"'
        initial_expr = p[3]
        condition_expr = p[5]
        update_expr = p[7]

        while condition_expr:
            # Execute statements inside the loop
            for statement in p[9]:
                execute_statement(statement)

            # Update loop variable or condition
            execute_expression(update_expr)

def p_whileLoop(p):
        'whileLoop : WHILE "(" condition ")" "{" statements "}"'
        pass
def p_error(p):
    print("Syntax error in input!")
    
    # Global variables or environment to store variable values
variables = {}

def execute_statement(statement):
    if isinstance(statement, tuple):
        if statement[0] == 'return':
            return execute_expression(statement[1])
        # Handle other types of statements as needed
    elif isinstance(statement, str):
        # Assuming it's a variable assignment statement
        execute_variable_assignment(statement)
    # Add more cases for other types of statements

def execute_variable_assignment(assignment_statement):
    identifier, value = assignment_statement.split("=")
    identifier = identifier.strip()
    value = execute_expression(value)
    variables[identifier] = value

def execute_expression(expression):
    if isinstance(expression, tuple):
        operator = expression[0]
        operand1 = execute_expression(expression[1])
        operand2 = execute_expression(expression[2])

        if operator == 'ADD':
            return operand1 + operand2
        elif operator == 'SUB':
            return operand1 - operand2
        elif operator == 'MUL':
            return operand1 * operand2
        elif operator == 'DIV':
            try:
                result = operand1 / operand2
            except ZeroDivisionError:
                print("Error: division by zero")
                result = None
            return result
        elif operator == 'OR':
            return operand1 or operand2
        elif operator == 'LE':
            return operand1 <= operand2
        elif operator == 'GE':
            return operand1 >= operand2
        elif operator == 'EQ':
            return operand1 == operand2
        elif operator == 'NE':
            return operand1 != operand2
        elif operator == 'GT':
            return operand1 > operand2
        elif operator == 'LT':
            return operand1 < operand2
    elif isinstance(expression, str):
        # Variable or literal value
        if expression in variables:
            return variables[expression]
        else:
            return eval(expression)  # Evaluate literal values
    else:
        return expression  # Literal value

    
parser = yacc.yacc()
input = open("input1.txt", "r") 
while True:
    try:
        s = input(input.read())
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
    
