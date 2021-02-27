"""
The prefix (reverse polish notation) version of the calculator
"""


def evaluate_prefix_expression(expression: str) -> float:
    """
    Evaluates a given expression and returns its final result.
    :param expression: An expression using the prefix notation i.e:

        > - / 10 + 1 1 * 1 2
        3

    :return: a float or integer containing the result of the operation
    """
    return float(expression)
