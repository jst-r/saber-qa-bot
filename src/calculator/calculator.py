from typing import Iterable

from src.calculator.constants import OPERATORS, OPERATORS_SET
from src.calculator.parser import infix_to_postfix, tokenize


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

def repr():
    print("Hello! This is a simple RPN calculator.")
    print(f"You can only input integers and following operations: {' '.join(OPERATORS_SET)}.")
    print("To exit the program type q")
    print("For example 1 + 2 * 3 + 1 / 2")

    while True:
        expr = input("Type your expression:\n")
        if expr.lower() == "q":
            break
        try:
            res = eval_str(expr)
            print(f"{expr} = {res}")
        except:
            print("Something went wrong")
    
    print("Bye!")

if __name__ == "__main__":
    repr()