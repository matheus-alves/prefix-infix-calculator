from calculator.prefix.prefix_calculator import evaluate_prefix_expression


class TestPrefixCalculator:
    def test_number_only_expression_returns_same_number(self):
        expression = '3'

        result = evaluate_prefix_expression(expression)

        assert result == float(expression)

    def test_simple_sum(self):
        expression = '+ 2 2'

        result = evaluate_prefix_expression(expression)

        assert result == 4

    def test_simple_subtraction(self):
        expression = '- 0 3'

        result = evaluate_prefix_expression(expression)

        assert result == -3

    def test_simple_multiplication(self):
        expression = '* 2 2'

        result = evaluate_prefix_expression(expression)

        assert result == 4

    def test_simple_division(self):
        expression = '/ 3 2'

        result = evaluate_prefix_expression(expression)

        assert result == 1.5

    def test_multiple_nested_operations_with_numbers_between_operators(self):
        expression = '+ 1 * 2 3'

        result = evaluate_prefix_expression(expression)

        assert result == 7

    def test_multiple_subsequent_operators(self):
        expression = '+ * 1 2 3'

        result = evaluate_prefix_expression(expression)

        assert result == 5

    def test_complex_operations_cases(self):
        expression = '- / 10 + 1 1 * 1 2'

        result = evaluate_prefix_expression(expression)

        assert result == 3

        expression = '+ * 2 3 / 4 2'

        result = evaluate_prefix_expression(expression)

        assert result == 8

        expression = '/ * 2 + 3 6 2'

        result = evaluate_prefix_expression(expression)

        assert result == 9

        expression = '* 2 + 2 / 2 2'

        result = evaluate_prefix_expression(expression)

        assert result == 6
