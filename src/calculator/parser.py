import re
from typing import Iterable, List, Union

from .constants import OPERATORS_SET, PRECEDENCE


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

        if token not in OPERATORS_SET:
            raise ValueError("Unknown operator")

        while stack and PRECEDENCE[token] <= PRECEDENCE[stack[-1]]:
            if token == stack[-1] == '^':
                break

            postfix.append(stack.pop())

        stack.append(token)

    while stack:
        postfix.append(stack.pop())

    return postfix
