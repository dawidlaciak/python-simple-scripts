import unittest
from bracket_counter import expressions_engine

class TestLongestCorrectExpressions(unittest.TestCase):

    def test_correct_expression(self):
        expression = "(a+b)*(a-b)/(c+d)"
        expected = ["(a+b)*(a-b)/(c+d)"]
        self.assertEqual(sorted(expressions_engine(expression)), sorted(expected))

    def test_one_invalid_parenthesis(self):
        expression = "(a+b)*(a-b))/(c+d)"
        expected = ["(a+b*(a-b))/(c+d)", "(a+b)*(a-b)/(c+d)"]
        self.assertEqual(sorted(expressions_engine(expression)), sorted(expected))

    def test_multiple_invalid_parentheses(self):
        expression = "((a+b))+(c+d))"
        expected = ["((a+b)+(c+d))", "((a+b))+(c+d)"]
        self.assertEqual(sorted(expressions_engine(expression)), sorted(expected))

    def test_no_parentheses(self):
        expression = "a+b*c"
        expected = ["a+b*c"]
        self.assertEqual(sorted(expressions_engine(expression)), sorted(expected))

    def test_empty_input(self):
        expression = ""
        expected = []
        self.assertEqual(sorted(expressions_engine(expression)), sorted(expected))

    def test_only_invalid_parentheses(self):
        expression = ")))((("
        expected = []
        self.assertEqual(sorted(expressions_engine(expression)), sorted(expected))

    def test_with_extra_characters(self):
        expression = "()x)"
        expected = ["()x", "(x)"]
        self.assertEqual(sorted(expressions_engine(expression)), sorted(expected))

    def test_nested_parentheses(self):
        expression = "((a+b)+(c+d))"
        expected = ["((a+b)+(c+d))"]
        self.assertEqual(sorted(expressions_engine(expression)), sorted(expected))

    def test_mixed_correct_and_incorrect_parentheses(self):
        expression = "((a+b))+(c+d))"
        expected = ['((a+b)+(c+d))', '((a+b))+(c+d)']
        self.assertEqual(sorted(expressions_engine(expression)), sorted(expected))

if __name__ == "__main__":
    unittest.main()
