import operator


OPERATORS = {'+': operator.add, '-': operator.sub, '*': operator.mul,
       '/': operator.truediv, '^': operator.pow}

OPERATORS_SET = set(OPERATORS.keys())
PRECEDENCE = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
