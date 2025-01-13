import unittest
from bracket_counter import find_longest_correct_expressions

class TestLongestCorrectExpressions(unittest.TestCase):

    def test_correct_expression(self):
        # Wyrażenie wejściowe już jest poprawne
        expression = "(a+b)*(a-b)/(c+d)"
        expected = ["(a+b)*(a-b)/(c+d)"]
        self.assertEqual(sorted(find_longest_correct_expressions(expression)), sorted(expected))

    def test_one_invalid_parenthesis(self):
        # Jedno dodatkowe zamknięcie nawiasu
        expression = "(a+b)*(a-b))/(c+d)"
        expected = ["(a+b*(a-b))/(c+d)", "(a+b)*(a-b)/(c+d)"]
        self.assertEqual(sorted(find_longest_correct_expressions(expression)), sorted(expected))

    def test_multiple_invalid_parentheses(self):
        # Wiele błędów w nawiasach
        expression = "((a+b))+(c+d))"
        expected = ["((a+b)+(c+d))", "((a+b))+(c+d)"]
        self.assertEqual(sorted(find_longest_correct_expressions(expression)), sorted(expected))

    def test_no_parentheses(self):
        # Brak nawiasów
        expression = "a+b*c"
        expected = ["a+b*c"]
        self.assertEqual(sorted(find_longest_correct_expressions(expression)), sorted(expected))

    def test_empty_input(self):
        # Pusty ciąg znaków
        expression = ""
        expected = []
        self.assertEqual(sorted(find_longest_correct_expressions(expression)), sorted(expected))

    def test_only_invalid_parentheses(self):
        # Same niepoprawne nawiasy
        expression = ")))((("
        expected = []
        self.assertEqual(sorted(find_longest_correct_expressions(expression)), sorted(expected))

    def test_with_extra_characters(self):
        # Błędy w nawiasach i dodatkowe znaki
        expression = "()x)"
        expected = ["()x", "(x)"]
        self.assertEqual(sorted(find_longest_correct_expressions(expression)), sorted(expected))

    def test_nested_parentheses(self):
        # Poprawne, ale zagnieżdżone nawiasy
        expression = "((a+b)+(c+d))"
        expected = ["((a+b)+(c+d))"]
        self.assertEqual(sorted(find_longest_correct_expressions(expression)), sorted(expected))

    def test_mixed_correct_and_incorrect_parentheses(self):
        # Mieszanka poprawnych i niepoprawnych nawiasów
        expression = "((a+b))+(c+d))"
        expected = ['((a+b)+(c+d))', '((a+b))+(c+d)']
        self.assertEqual(sorted(find_longest_correct_expressions(expression)), sorted(expected))

if __name__ == "__main__":
    unittest.main()
