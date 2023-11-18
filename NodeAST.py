class Node:
    def __init__(self, type, children=None, leaf=None):
        self.type = type
        if children:
            self.children = children
        else:
            self.children = []
        self.leaf = leaf

    
    def to_string(self, level=0):
        ret = "\t" * level + repr(self.children) +repr(self.leaf) + "\n"
        for child in self.children:
            ret += child.to_string(level + 1)
        return ret

    def semantic_analysis(self):
        raise NotImplementedError("Subclass must implement semantic_analysis")
    
    def evaluate(self):
        raise NotImplementedError("Subclass must implement evaluate")

    
class ProgramNode(Node):
    def __init__(self, program_start):
        super().__init__('program', children=[program_start], leaf='program')

    
    def to_string(self, level=0):
        return super().to_string(level+1)

    def semantic_analysis(self):
        # Perform semantic analysis on the program start
        pass

class ProgramStartNode(Node):
    def __init__(self, function_declarations):
        super().__init__('program_start', children=[function_declarations], leaf='program_start')

    def to_string(self, level=0):
        return super().to_string(level+1) 
    
    def semantic_analysis(self):
        # Perform semantic analysis on the function declarations
        pass
    
class BinOpNode(Node):
    def __init__(self, operator, left, right):
        super().__init__('binop', children=[left, right], leaf=operator)

    def to_string(self, level=0):
        return super().to_string(level+1)
    
    def semantic_analysis(self):
        # Perform semantic analysis on the operands
        for child in self.children:
            child.semantic_analysis()

        # Check that the operands are of the correct type
        left_type = type(self.children[0].leaf)
        right_type = type(self.children[1].leaf)

        if self.leaf in ['ADD', 'SUB', 'MUL', 'DIV']:
            if not (left_type in [int, float] and right_type in [int, float]):
                raise TypeError("Operands must be integers or floats for arithmetic operations")
        elif self.leaf in ['GE', 'LE', 'EQ', 'NE', 'GT', 'LT']:
            if not (left_type == right_type):
                raise TypeError("Operands must be of the same type for comparison operations")
        else: 
            print("Semantic analysis completed successfully")

    def evaluate(self):
            left_value = self.children[0].evaluate()
            right_value = self.children[1].evaluate()

            if self.leaf == 'ADD':
                return left_value + right_value
            elif self.leaf == 'SUB':
                return left_value - right_value
            elif self.leaf == 'MUL':
                return left_value * right_value
            elif self.leaf== 'DIVIDE':
                if right_value != 0:
                    return left_value / right_value
                else:
                    raise ValueError("Division by zero")
        
    
    
class UnOpNode(Node):
    def __init__(self, operator, operand):
        super().__init__('unop', children=[operand], leaf=operator)

    def to_string(self, level=0):
        return super().to_string(level+1)
    
    def semantic_analysis(self):
        # Perform semantic analysis on the operand
        pass

        # Check that the operand is of the correct type
        operand_type = type(self.children[0].leaf)

        if self.leaf == 'UNARY':
            if not (operand_type in [int, float]):
                raise TypeError("Operand must be an integer or float for unary operation")

    def evaluate(self):
        operand_value = self.children[0].evaluate()

        if self.leaf == 'UNARY':
            return -operand_value
        
    
    
class IntNode(Node):
    def __init__(self, value):
        super().__init__('int', leaf=int(value))

    def to_string(self, level=0):
        return super().to_string(level+1)
    
    def semantic_analysis(self):
        if isinstance(self.leaf, float):
            raise TypeError("IntNode must be an integer")

    def evaluate(self):
        return self.leaf
    
  
    
class FloatNode(Node):
    def __init__(self, value):
        super().__init__('float', leaf=float(value))

    def to_string(self, level=0):
        return super().to_string(level+1)
    
    def semantic_analysis(self):
        if not isinstance(self.leaf, float):
            raise TypeError("FloatNode must be a float")
            
    def evaluate(self):
        return self.leaf
    

class StringNode(Node):
    def __init__(self, value):
        super().__init__('string', leaf=str(value))

    def to_string(self, level=0):
        return super().to_string(level+1)
    
    def semantic_analysis(self):
        if not isinstance(self.leaf, str):
            raise TypeError("StringNode must be a string")

    def evaluate(self):
        return self.leaf
    
    
class IdentifierNode(Node):
    def __init__(self, value):
        super().__init__('identifier', leaf=str(value))

    def to_string(self, level=0):
        return super().to_string(level+1)
    
    def semantic_analysis(self):
        if not isinstance(self.leaf, str):
            raise TypeError("IdentifierNode must be a string")

    def evaluate(self):
        return self.leaf
    
    
class AssignmentNode(Node):
    def __init__(self, datatype, identifier, expression):
        super().__init__('assignment', children=[datatype, identifier, expression], leaf='=')

    def to_string(self, level=0):
        return super().to_string(level+1)
    
    def semantic_analysis(self):
        # Perform semantic analysis on the expression
        self.children[2].semantic_analysis()

        # Check that the identifier is of the correct type
        identifier_type = self.children[0].leaf
        expression_type = type(self.children[2].leaf)

        if identifier_type == 'INT':
            if not (expression_type in [int, float]):
                raise TypeError("Identifier must be an integer or float for assignment")
        elif identifier_type == 'FLOAT':
            if not (expression_type in [int, float]):
                raise TypeError("Identifier must be an integer or float for assignment")
        elif identifier_type == 'STRING':
            if not (expression_type in [str]):
                raise TypeError("Identifier must be a string for assignment")
      
    
class ConditionNode(Node):
    def __init__(self, condition, if_body, else_body):
        super().__init__('condition', children=[condition, if_body, else_body], leaf='if')
    
    def to_string(self, level=0):
        return super().to_string(level+1)
    
    def semantic_analysis(self):
        # Perform semantic analysis on the condition
        pass

        # Check that the condition is of the correct type
        condition_type = type(self.children[0].leaf)

        if not (condition_type in [bool]):
            raise TypeError("Condition must be a boolean")



        # Perform semantic analysis on the else body
        self.children[2].semantic_analysis()

class LoopNode(Node):
    def __init__(self, condition, body):
        super().__init__('loop', children=[condition, body], leaf='loop')

    def to_string(self, level=0):
        return super().to_string(level+1)
    
    def semantic_analysis(self):
        # Perform semantic analysis on the condition
        pass

        # Check that the condition is of the correct type
        condition_type = type(self.children[0].leaf)

        if not (condition_type in [bool]):
            raise TypeError("Condition must be a boolean")
    
class ReturnNode(Node):
    def __init__(self, expression):
        super().__init__('return', children=[expression], leaf='return')

    def to_string(self, level=0):
        return super().to_string(level+1)
    
    def semantic_analysis(self):
        # Perform semantic analysis on the expression
        pass

        # Check that the expression is of the correct type
        expression_type = type(self.children[0].leaf)

        if not (expression_type in [int, float, str]):
            raise TypeError("Return value must be an integer, float or string")
        
class PrintNode(Node):
    def __init__(self, expression):
        super().__init__('print', children=[expression], leaf='print')

    def to_string(self, level=0):
        return super().to_string(level+1)
    
    def semantic_analysis(self):
        # Perform semantic analysis on the expression
        pass

        # Check that the expression is of the correct type
        # expression_type = type(self.children[0].leaf)

        # if not (expression_type in [int, float, str]):
        #     raise TypeError("Print value must be an integer, float or string")
        
class FunctionCallNode(Node):
    def __init__(self, identifier, parameters):
        super().__init__('function_call', children=[identifier, parameters], leaf='function_call')

    def to_string(self, level=0):
        return super().to_string(level+1)
    
    def semantic_analysis(self):
        # Check that the parameters are of the correct type
        parameters_type = type(self.children[1].leaf)

        if not (parameters_type in [int, float, str]):
            raise TypeError("Parameters must be an integer, float or string")
        
class FunctionsDeclarationsNode(Node):
    def __init__(self, function_declaration, function_declarations):
        super().__init__('function_declarations', children=[function_declaration, function_declarations], leaf='function_declarations')

    def to_string(self, level=0):
        return super().to_string(level+1)
    
    def semantic_analysis(self):
        # Perform semantic analysis on the function declaration
        pass

        # Perform se

class FunctionDeclarationNode(Node):
    def __init__(self, identifier, parameters, body):
        super().__init__('function_declaration', children=[identifier, parameters, body], leaf='function_declaration')

    def to_string(self, level=0):
        return super().to_string(level+1)
    
    def semantic_analysis(self):
        #

        # Check that the parameters are of the correct type
        parameters_type = type(self.children[1].leaf)

        if not (parameters_type in [int, float, str]):
            raise TypeError("Parameters must be an integer, float or string")

        # Perform semantic analysis on the body
        self.children[2].semantic_analysis()


class ParameterNode(Node):
    def __init__(self, datatype, identifier):
        super().__init__('parameter', children=[datatype, identifier], leaf='parameter')
    def to_string(self, level=0):
        return super().to_string(level+1)
    
    def semantic_analysis(self):
        #

        # Check that the identifier is of the correct type
        identifier_type = type(self.children[1].leaf)

        if not (identifier_type in [int, float, str]):
            raise TypeError("Identifier must be an integer, float or string")

class ParameterListNode(Node):
    def __init__(self, parameter, parameter_list):
        super().__init__('parameter_list', children=[parameter, parameter_list], leaf='parameter_list')

    def to_string(self, level=0):
        return super().to_string(level+1)
    
    def semantic_analysis(self):
        # Perform semantic analysis on the parameter
        pass

        # Per
class ParametersNode(Node):
    def __init__(self, parameter_list):
        super().__init__('parameters', children=[parameter_list], leaf='parameters')

    def to_string(self, level=0):
        return super().to_string(level+1)
    
    def semantic_analysis(self):
        # Perform semantic analysis on the parameter list
        pass

class DatatypeNode(Node):
    def __init__(self, datatype):
        super().__init__('datatype', leaf=datatype)

    def to_string(self, level=0):
        return super().to_string(level+1)
    
    def semantic_analysis(self):
        # Check that the datatype is of the correct type
        if not (self.leaf in [['int'], ['float'], ['string']]):
            raise TypeError("Datatype must be an integer, float or string")

class StatementsNode(Node):
    def __init__(self, statement=None, statements=None):
        super().__init__('statements', children=[statement, statements], leaf='statements')


    def to_string(self, level=0):
        return super().to_string(level+1)
    
    def semantic_analysis(self):
        # Perform semantic analysis on the statement
        pass

        #

class StatementNode(Node):
    def __init__(self, statement):
        super().__init__('statement', children=[statement], leaf='statement')

    def to_string(self, level=0):
        return super().to_string(level+1)
    
    def semantic_analysis(self):
        # Perform semantic analysis on the statement
        pass

class FunctionBodyNode(Node):
    def __init__(self, statements):
        super().__init__('function_body', children=[statements], leaf='function_body')

    def to_string(self, level=0):
        return super().to_string(level+1)
    
    def semantic_analysis(self):
        # Perform semantic analysis on the statements
        pass

class ExpressionNode(Node):
    def __init__(self, expression):
        super().__init__('expression', children=[expression], leaf='expression')

    def to_string(self, level=0):
        return super().to_string(level+1)
    
    def semantic_analysis(self):
        # Perform semantic analysis on the expression
        pass

class AtomsNode(Node):
    def __init__(self, atom):
        super().__init__('atoms', children=atom, leaf='atoms')

    def to_string(self, level=0):
        return super().to_string(level+1)

    def semantic_analysis(self):
        # Perform semantic analysis on the atom
        pass 
    

class VariableNode(Node):
    def __init__(self, identifier):
        super().__init__('variable', children=[identifier], leaf='variable')

    def to_string(self, level=0):
        return super().to_string(level+1)
    
    def semantic_analysis(self):
        # Perform semantic analysis on the identifier
        pass

class ParentExprNode(Node):
    def __init__(self, expression):
        super().__init__('paren_expr', children=[expression], leaf='paren_expr')

    def to_string(self, level=0):
        return super().to_string(level+1)
    
    def semantic_analysis(self):
        # Perform semantic analysis on the expression
        pass

class ForLoopNode(Node):
    def __init__(self, assignment, condition, assignment2, body):
        super().__init__('for_loop', children=[assignment, condition, assignment2, body], leaf='for_loop')

    def to_string(self, level=0):
        return super().to_string(level+1)
    
    def semantic_analysis(self):
        pass

class WhileLoopNode(Node):
    def __init__(self, condition, body):
        super().__init__('while_loop', children=[condition, body], leaf='while_loop')
    
    def to_string(self, level=0):
        return super().to_string(level+1)
    
    def semantic_analysis(self):
        # Perform semantic analysis on the condition
        pass






