from src.calculator.constants import OPERATORS_SET


AUTH_SUCCESS = f"""
    Вы успешно вошли в калькулятор!
    Он поддерживает только целые числа и операции {' '.join(OPERATORS_SET)}
    Пример валидного выражения:
    1 + 2 * 3 + 1 / 2
"""

AUTH_FAIL = """
    Пароль не верный. Попробуйте "The most secure password ever!!!11!1"
"""