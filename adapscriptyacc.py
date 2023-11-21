# #Parser for AdapScript language
# import ply.yacc as yacc
# from adapscriptlexer import tokens
# import logging



# logging.basicConfig(
#     level=logging.DEBUG,
#     filename="parselog.txt",
#     filemode="w",
#     format="%(filename)10s:%(lineno)4d:%(message)s"
# )

# symbolTable = {}
# precedence = (
#     ('left', 'ADD', 'SUB'),
#     ('left', 'MUL', 'DIV'),
#     # ('right','UMINUS')
#     ('nonassoc','GE', 'LE', 'EQ', 'NE', 'GT', 'LT', 'OR'),

# )



# def p_program(p):
#     '''program : programStart'''
#     p[0] = ('program',p[1])

# def p_programStart(p):
#     '''programStart : FUNC INIT "(" ")" "{" statements "}" '''
#     p[0] = ('programStart',p[6])
    
# def p_statements(p):
#     '''statements : statement
#                 | statements statement
#                 '''
#     if len(p) == 2:
#         p[0] = p[1]
#     else:
#         p[0] = ('statements',p[1],p[2])
                 
# def p_statement(p):
#     '''statement : function_calls
#                 | condition
#                 | function_declarations
#                 | expression
#                 | loops
#                 | RETURN expression
#                 | PRINT "(" expression ")"
#                 | assignment
#                 '''
#     if len(p) == 2:
#         # p[0] = StatementNode(p[1])
#         p[0] =p[1]
#     elif len(p) == 3:
#         # p[0] = StatementNode(ReturnNode(p[2]))
#         p[0] = p[2]

#     else:
#         p[0] = print(p[3])
                
                
# def p_function_declarations(p):
#         '''function_declarations : function_declaration 
#                                  | function_declarations function_declaration'''
#         # p[0] = FunctionsDeclarationsNode(p[1])
#         p[0]=('declarations', p[1])

# def p_function_declaration(p):
#         '''function_declaration : FN IDENTIFIER "(" ")" ":" datatype "{" function_body "}" 
#                                 | FN IDENTIFIER "(" parameters ")" ":" datatype "{" function_body "}" '''
        
#         if len(p) == 9:
#             # p[0] = FunctionDeclarationNode(p[2], p[6], p[8])
#             p[0]= ('declaration', p[2], p[6], p[8])
#         else:
#             # p[0] = FunctionDeclarationNode(p[2], p[7])
#             p[0]= ('declaration', p[2],p[8])

        

# def p_function_body(p):
#         '''function_body : statements'''
#         # p[0] = FunctionBodyNode(p[1])
#         p[0]= p[1]


# def p_function_calls(p):
#     '''function_calls : IDENTIFIER "(" ")"
#                      | IDENTIFIER "(" ")" function_calls
#                      | IDENTIFIER "(" parameters ")" 
#                      | IDENTIFIER "(" parameters ")" function_calls'''
#     if len(p) == 4:
#         # p[0] = FunctionCallNode(p[1])
#         p[0]= (p[1], p[3], p[4])

#     elif len(p) == 2:
#         # p[0] = FunctionCallNode(p[1], p[3])
#         p[0]=  p[1]


                     
# def p_parameters(p):
    
#     '''parameters : parameterList'''
#     # p[0] = ParametersNode([p[1]])
#     p[0]= p[1]

# def p_parameterList(p):
#     '''parameterList : parameter
#                     | parameter "," parameterList'''
#     if len(p) == 2:
#         # p[0] = ParameterListNode(p[1])
#         p[0]= p[1]
#     else:
#         # p[0] = ParameterListNode(p[1], p[3])
#         p[0]= ('parameterlist', p[1], p[3])

# def p_parameter(p):
#     '''parameter : IDENTIFIER
#                 | datatype IDENTIFIER'''
#     if len(p) == 2:
#         # p[0] = ParameterNode(p[1])
#         p[0]= p[1]
#     else:
#         # p[0] = ParameterNode(p[1], p[2])
#         p[0]= ('parameter', p[1], p[2])

# def p_datatype(p):
#         '''datatype : INT
#                     | FLOAT
#                     | STRING
#                     | ADAPT
#                     | VOID'''
#         # p[0] = DatatypeNode([p[1]])
#         p[0]= p[1]
                    
# def p_binary_expr(p):
#         '''expression : expression ADD expression
#                     | expression SUB expression
#                     | expression MUL expression
#                     | expression DIV expression
#                     | expression OR expression
#                     | expression LE expression
#                     | expression GE expression
#                     | expression EQ expression
#                     | expression NE expression
#                     | expression GT expression
#                     | expression LT expression
#                     | atoms expression
                    
#                     '''
#         p[0]= ('binop', p[1], p[2], p[3])

# def p_expression_group(t):
#     '''
#     expression : "(" expression ")"
#     '''
#     t[0] = t[2] 

# # def p_expression_uminus(p):
# #     '''expression : SUB expression %prec UMINUS'''
# #     p[0] = ('unminus',p[2])



            
# def p_atom(p):
#         '''atoms : INT_VALUE
#                 | FLOAT_VALUE
#                 | STRING_VALUE
#                 | variable'''
#         if isinstance(p[1], int):
#             # p[0] = IntNode(p[1])   
#             p[0]= p[1]
#         elif isinstance(p[1], float):
#             # p[0] = FloatNode(p[1])
#             p[0]= p[1]
#         elif isinstance(p[1], str):
#             # p[0] = StringNode(p[1])
#             p[0]= p[1]
#         else:
#             # p[0] = VariableNode(p[1]) 
#             p[0]= p[1]
# def p_variable(p):
#     '''variable : IDENTIFIER '''
#     # p[0] = VariableNode(p[1])
#     p[0]= ('variable', p[1])

      
# def p_assignment(p):    
#         '''assignment : datatype IDENTIFIER EQUAL expression 
#                       | datatype IDENTIFIER EQUAL function_calls
#                       | datatype IDENTIFIER EQUAL ACCEPT "(" ")" '''
#         # p[0] = AssignmentNode(p[1], p[2], p[4])
#         p[0]= ('assignment', p[1], p[2], p[4])

# def p_condition(p):
#         '''condition : IF expreesion "{" statements "}"
#                     | IF expression "{" statements "}" ELSE "{" statements "}"'''
                    
#         if len(p) == 6:
#             # p[0] = ConditionNode(p[2], p[4])
#             p[0]= ('condition', p[2], p[4])
#         else:
#             # p[0] = ConditionNode(p[2], p[4], p[8])
#             p[0]= ('condition', p[2], p[4], p[8])

# def p_loops(p):
#         '''loops : loop
#                 | loop loops'''
#         if len(p) == 2:
#             # p[0] = Node(p[1])
#             p[0]= p[1]
#         else:
#             # p[0] = Node(p[1], p[2])
#             p[0]= ('loop', p[1], p[2])
        

# def p_loop(p):
#         '''loop : forLoop
#                 | whileLoop'''
#         # p[0] = LoopNode('loop',p[1])
#         p[0]= p[1]
        

# def p_forLoop(p):
#         '''forLoop : FOR "(" assignment ";" expression ";" expression ")" "{" statements "}"'''
#         # p[0] = ForLoopNode(p[5],p[7],p[9],p[10])
#         p[0]= ('forloop', p[5], p[7], p[9], p[10])

# def p_whileLoop(p):
#         '''whileLoop : assignment WHILE "(" expression ")" "{" statements "}"'''
#         # p[0] = WhileLoopNode(p[4], p[7])
#         p[0]= ('whileloop', p[4], p[7])

# def p_error(p):
#     print(f"Syntax error at line {p.lineno}, position {p.lexpos}: Unexpected token '{p.value}' '{p.type}''")
   

# tree = []
    

# def printTree(action, level=0):
#     tree.append(action)
#     print(action)
#     if isinstance(action, tuple):
#         for child in action:
#             if isinstance(child, tuple):
#                 printTree(child, level + 1)
#             else:
#                 print(child)
#         if action[0] == 'binop':
#             result = code_binaryExpr(action)
#             print(f"Result of binary operation: {result}")

     
# def code_binaryExpr(action):
#     if action[2]== '+':
#         return action[1] + action[3]
#     elif action[2]== '-':
#         return action[1] - action[3]
#     elif action[2]== '*':
#         return action[1] * action[3]
#     elif action[2]== '/':
#         return action[1] / action[3]
    
     
    
    





# log = logging.getLogger()
# parser = yacc.yacc(debug=True, debuglog=log )
# inputFile = open('input3.txt', 'r')
# data = inputFile.read()
# inputFile.close()
# ast = parser.parse(data)
# printTree(ast)
# print(ast)









    
    
    
