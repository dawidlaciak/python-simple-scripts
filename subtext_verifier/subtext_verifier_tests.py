import unittest

from subtext_verifier import check_subtext

class TestCheckSubtext(unittest.TestCase):

    def test_exact_match(self):
        self.assertTrue(check_subtext("abc", "abc"))

    def test_subtext_at_start(self):
        self.assertTrue(check_subtext("abc", "abcdef"))

    def test_subtext_at_end(self):
        self.assertTrue(check_subtext("def", "abcdef"))

    def test_subtext_in_middle(self):
        self.assertTrue(check_subtext("bcd", "abcdef"))

    def test_non_subtext(self):
        self.assertFalse(check_subtext("xyz", "abcdef"))

    def test_empty_text_a(self):
        self.assertTrue(check_subtext("", "abcdef"))

    def test_empty_text_b(self):
        self.assertFalse(check_subtext("abc", ""))

    def test_case_insensitivity(self):
        self.assertTrue(check_subtext("ABC", "abcdef"))

    def test_with_spaces_in_text_a(self):
        self.assertFalse(check_subtext("a c", "abcdef"))

    def test_with_spaces_in_text_b(self):
        self.assertTrue(check_subtext("abc", "a b c d e f"))

    def test_both_empty_strings(self):
        self.assertTrue(check_subtext("", ""))

if __name__ == "__main__":
    unittest.main()