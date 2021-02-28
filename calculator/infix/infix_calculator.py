"""
The infix version of the calculator
"""
from typing import List

from calculator.base_calculator_operations import SYMBOLS, OPERATIONS

END_PARENTHESIS = ')'
START_PARENTHESIS = '('


def do_evaluate(tokens: List) -> float:
    """
    Recursive function to evaluate the expression
    :param tokens: the list of tokens
    :return: the result of the operation from recursive calls
    """
    current_args = list()

    while tokens:
        token = tokens.pop(0)

        if token == START_PARENTHESIS:
            current_args.append(do_evaluate(tokens))

        if token in SYMBOLS:
            operation = OPERATIONS[token]

        if token.isdigit():
            current_args.append(int(token))

        if token == END_PARENTHESIS:
            break

    return operation(current_args.pop(0), current_args.pop(0)) \
        if len(current_args) == 2 else current_args.pop()


def evaluate_infix_expression(expression: str) -> float:
    """
    Evaluates a given expression and returns its final result.
    :param expression: An expression using the infix notation i.e:

        > ( ( ( 1 + 1 ) / 10 ) - ( 1 * 2 ) )
        -1.8

    :return: a float or integer containing the result of the operation
    """
    tokens = expression.split()
    return do_evaluate(tokens)
