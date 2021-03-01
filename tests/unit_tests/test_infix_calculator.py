from calculator.model.infix.infix_calculator import evaluate_infix_expression


class TestInfixCalculator:
    def test_simple_sum(self):
        expression = '( 2 + 2 )'

        result = evaluate_infix_expression(expression)

        assert result == 4

    def test_simple_subtraction(self):
        expression = '( 0 - 3 )'

        result = evaluate_infix_expression(expression)

        assert result == -3

    def test_simple_multiplication(self):
        expression = '( 2 * 2 )'

        result = evaluate_infix_expression(expression)

        assert result == 4

    def test_simple_division(self):
        expression = '( 3 / 2 )'

        result = evaluate_infix_expression(expression)

        assert result == 1.5

    def test_nested_operations_cases(self):
        expression = '( 1 + ( 2 * 3 ) )'

        result = evaluate_infix_expression(expression)

        assert result == 7

        expression = '( ( 1 * 2 ) + 3 )'

        result = evaluate_infix_expression(expression)

        assert result == 5

    def test_complex_multiple_operations_cases(self):
        expression = '( ( ( 1 + 1 ) / 10 ) - ( 1 * 2 ) )'

        result = evaluate_infix_expression(expression)

        assert result == -1.8

        expression = '( 2 * ( 3 + ( 4 / 2 ) ) )'

        result = evaluate_infix_expression(expression)

        assert result == 10

        expression = '( ( 2 * 3 ) + ( 6 / 2 ) )'

        result = evaluate_infix_expression(expression)

        assert result == 9

        expression = '( ( 2 * ( 2 + 2 ) ) / 2 )'

        result = evaluate_infix_expression(expression)

        assert result == 4
