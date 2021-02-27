from calculator.prefix.prefix_calculator import evaluate_prefix_expression


class TestPrefixCalculator:
    def test_number_only_expression_returns_same_number(self):
        expression = "3"

        result = evaluate_prefix_expression(expression)

        assert result == float(expression)
