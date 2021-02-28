"""
The prefix (reverse polish notation) version of the calculator
"""
from typing import List

from calculator.base_calculator_operations import SYMBOLS, OPERATIONS


def do_evaluate(tokens: List) -> float:
    """
    Recursive function to evaluate the expression
    :param tokens: the list of tokens
    :return: either the token itself converted to integer
    or the result of the operation from recursive calls
    """
    token = tokens.pop(0)

    if token in SYMBOLS:
        operation = OPERATIONS[token]
        return operation(do_evaluate(tokens), do_evaluate(tokens))

    return int(token)


def evaluate_prefix_expression(expression: str) -> float:
    """
    Evaluates a given expression and returns its final result.
    :param expression: An expression using the prefix notation i.e:

        > - / 10 + 1 1 * 1 2
        3

    :return: a float or integer containing the result of the operation
    """
    tokens = expression.split()

    return do_evaluate(tokens)
