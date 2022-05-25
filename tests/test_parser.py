from src.calculator.parser import tokenize, infix_to_postfix


def test_tokenize():
    assert tokenize("1") == ["1"]
    assert tokenize("1+1") == ["1", "+", "1"]
    assert tokenize("1 + 3 * 2") == ["1", "+", "3", "*", "2"]

def test_infix_to_postfix():
    assert infix_to_postfix(["1"]) == ["1"]
    assert infix_to_postfix(["1", "+", "1"]) == ["1", "1", "+"]
    assert infix_to_postfix(["1", "+", "3", "*", "2"]) == ["1", "3", "2", "*", "+"]