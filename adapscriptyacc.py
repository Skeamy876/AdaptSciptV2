#Parser for AdapScript language
import ply.yacc as yacc
from adapscriptlexer import tokens
from NodeAST import*
from openai import OpenAI

clientLLM = OpenAI()
sym_Table = {}
precedence = (
    ('nonassoc','GE', 'LE', 'EQ', 'NE', 'GT', 'LT', 'OR'),
    ('left', 'ADD', 'SUB'),
    ('left', 'MUL', 'DIV'),
    ('right', 'UNARY')
)


def p_program(p):
    '''program : programStart'''
    p[0] = ProgramNode([p[1]])

def p_programStart(p):
    '''programStart : FUNC INIT "(" ")" "{" statements "}" '''
    p[0] = ProgramStartNode([p[6]])
    
def p_statements(p):
    '''statements : statement
                | statements statement
                '''
    if len(p) == 2:
        p[0] = StatementsNode([p[1]])
    else:
        p[0] = StatementsNode([p[1]],[p[2]])
                 
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
    if len(p) == 2:
        p[0] = StatementNode([p[1]])
    elif len(p) == 3:
        p[0] = StatementNode(ReturnNode([p[2]]))
    else:
        p[0] = StatementNode(PrintNode([p[3]]))
                
                
def p_function_declarations(p):
        '''function_declarations : function_declaration'''
        p[0] = FunctionsDeclarationsNode([p[1]])

def p_function_declaration(p):
        '''function_declaration : FUNC IDENTIFIER "(" ")" ":" datatype "{" function_body "}" '''
        p[0] = FunctionDeclarationNode([p[2], p[7]])
        

def p_function_body(p):
        '''function_body : statements'''
        p[0] = FunctionBodyNode([p[1]])

def p_function_calls(p):
    '''function_calls : IDENTIFIER "(" ")"
                     | IDENTIFIER "(" ")" function_calls
                     | IDENTIFIER "(" parameters ")" 
                     | IDENTIFIER "(" parameters ")" function_calls'''
    if len(p) == 4:
        p[0] = FunctionCallNode([p[1]])
    else:
        p[0] = FunctionCallNode([p[1], p[3]])
                     
def p_parameters(p):
    '''parameters : parameterList'''
    p[0] = ParametersNode([p[1]])

def p_parameterList(p):
    '''parameterList : parameter
                    | parameter "," parameterList'''
    if len(p) == 2:
        p[0] = ParameterListNode([p[1]])
    else:
        p[0] = ParameterListNode([p[1], p[3]])

def p_parameter(p):
    '''parameter : datatype IDENTIFIER'''
    p[0] = ParameterNode([p[1], p[2]])

def p_datatype(p):
        '''datatype : INT
                    | FLOAT
                    | STRING
                    | ADAPT
                    | VOID'''
        p[0] = DatatypeNode([p[1]])
                    

def p_expression(p):
        '''expression : atoms
                    | paren_expr
                    | binary_expr'''
        p[0] = ExpressionNode([p[1]])
            
def p_atom(p):
        '''atoms : INT_VALUE
                | FLOAT_VALUE
                | STRING_VALUE
                | variable'''
        if isinstance(p[1], int):
            p[0] = IntNode(p[1])   
        elif isinstance(p[1], float):
            p[0] = FloatNode(p[1])
        elif isinstance(p[1], str):
            p[0] = StringNode([p[1]])
        else:
            p[0] = VariableNode([p[1]]) 

def p_variable(p):
    '''variable : IDENTIFIER '''
    p[0] = VariableNode([p[1]])

def p_paren_expr(p):
        '''paren_expr : "(" expression ")"'''
        p[0] = ParentExprNode([p[2]])

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
        p[0] = AssignmentNode(p[1], p[2], p[4])

def p_condition(p):
        '''condition : IF expression "{" statements "}"
                    | IF expression "{" statements "}" ELSE "{" statements "}"'''
        if len(p) == 6:
            p[0] = ConditionNode([p[2], p[4]])
        else:
            p[0] = ConditionNode([p[2], p[4], p[8]])

def p_loops(p):
        '''loops : loop
                | loop loops'''
        if len(p) == 2:
            p[0] = Node([p[1]])
        else:
            p[0] = Node([p[1], p[2]])
        

def p_loop(p):
        '''loop : forLoop
                | whileLoop'''
        p[0] = LoopNode('loop',[p[1]])
        

def p_forLoop(p):
        '''forLoop : FOR "(" INT IDENTIFIER EQUAL INT_VALUE ";" condition ";" expression ")" "{" statements "}"'''
        p[0] = ForLoopNode([p[3], p[5], p[7], p[10]])

def p_whileLoop(p):
        '''whileLoop : WHILE "(" condition ")" "{" statements "}"'''
        p[0] = WhileLoopNode([p[3], p[6]])

def p_error(p):
    print(f"Syntax error at line {p.lineno}, position {p.lexpos}: Unexpected token '{p.value}'")
   

tree = []
def printTree(node, level=0):
    if isinstance(node, list):
        for subnode in node:
            printTree(subnode, level)
    else:
        tree.append(node)
        print('\t' * level + str(node))
        if hasattr(node, 'children'):
            if is_iterable(node.children):
                for child in node.children:
                    if hasattr(child, 'children'):   
                         break  
                    else:
                        for i in child:
                            if i.type == 'binop': 
                                i.semantic_analysis()          
                    printTree(child, level + 1)
                    break
                node.semantic_analysis()
                printTree(node.children, level + 1)
    return tree

def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

parser = yacc.yacc()
inputFile = open('input3.txt', 'r')
data = inputFile.read()
inputFile.close()
ast = parser.parse(data)

printTree(ast)









    
    
    
