from src.calculator.calculator import eval_RPN, eval_str


def test_eval_RPN():
    assert eval_RPN(["1", "1", "+"]) == 1 + 1
    assert eval_RPN(["1", "3", "2", "*", "+"]) == 1 + 3 * 2
    assert eval_RPN(['1', '2', '/']) == 1/2
    assert eval_RPN(['3', '1', '2', '/', '*']) == 3/2
    assert eval_RPN(['2', '3', '2', '^', '^']) == 2 ** 3 ** 2

def test_eval_str():
    assert eval_str("1 + 2") == 3
    assert eval_str("1 / 2 * 2 + 1") == 2
    assert eval_str("1 + 3 * 2") == 7
    assert eval_str("2 ^ 2 + 3 ^ 2") == 13