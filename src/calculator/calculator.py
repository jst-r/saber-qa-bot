from typing import Iterable

from .constants import OPERATORS
from .parser import infix_to_postfix, tokenize


def eval_RPN(rpn: Iterable[str]):
    stack = []
    
    for token in rpn:
        if token.isnumeric():
            stack.append(float(token))
            continue
        
        b, a = [stack.pop(), stack.pop()]
        c = OPERATORS[token](a, b)
        stack.append(c)
    
    if len(stack) != 1:
        raise ValueError("Invalid expression")
    
    return stack[0]

def eval_str(expr: str):
    tokens = tokenize(expr)
    rpn = infix_to_postfix(tokens)
    return eval_RPN(rpn)