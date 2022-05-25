import re
from typing import Iterable, List, Union

OPERATORS = set(['+', '-', '*', '/', '^'])
PRECEDENCE = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}


def tokenize(expr: str) -> List[int]:
    '''
    Splits input string into tokens.
    Token is a number or an operator.
    '''
    pattern = re.compile(r"([0-9]+|[\+\-\*/\^])")
    return re.findall(pattern, expr)


def infix_to_postfix(infix: Iterable[str]):
    stack = []
    postfix = []

    for token in infix:
        if token.isnumeric():
            postfix.append(token)
            continue

        while stack and PRECEDENCE[token] <= PRECEDENCE[stack[-1]]:
            if token == stack[-1] == '^':
                break

            postfix.append(stack.pop())
        
        stack.append(token)

    while stack:
        postfix.append(stack.pop())
    
    return postfix

