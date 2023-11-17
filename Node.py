class Node:
    def __init__(self, type, children=None, leaf=None):
        self.type = type
        if children:
            self.children = children
        else:
            self.children = []
        self.leaf = leaf

    def semantic_analysis(self):
        raise NotImplementedError("Subclass must implement semantic_analysis")
    
class BinOpNode(Node):
    def __init__(self, operator, left, right):
        super().__init__('binop', children=[left, right], leaf=operator)

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


