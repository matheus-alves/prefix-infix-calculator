"""
This module contains the domain layer logic of the calculator.
It works as an entry point for the api calls.
"""

from calculator.model.prefix.prefix_calculator import evaluate_prefix_expression
from calculator.model.infix.infix_calculator import evaluate_infix_expression


PREFIX_NOTATION = 'prefix'
INFIX_NOTATION = 'infix'


def evaluate_expression(expression: str, notation: str) -> float:
    """
    Calculates the expression result given its notation.
    :param expression: The expression to be calculated
    :param notation: The notation type that the expression is written in. I.e. (prefix, infix)
    :return: The result of the expression
    """
    if notation == PREFIX_NOTATION:
        return evaluate_prefix_expression(expression)

    if notation == INFIX_NOTATION:
        return evaluate_infix_expression(expression)

    raise Exception("Invalid notation type")
