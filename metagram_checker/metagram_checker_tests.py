import unittest

from metagram_checker import metagram_checker

class TestCheckSubtext(unittest.TestCase):

    def test_identical_words(self):
        self.assertFalse(metagram_checker("test", "test"))

    def test_first_metagram(self):
        self.assertTrue(metagram_checker("kasa", "kara"))

    def test_second_metagram(self):
        self.assertTrue(metagram_checker("spin", "spit"))

    def test_not_metagram(self):
        self.assertFalse(metagram_checker("test", "mast"))

    def test_different_lengths(self):
        self.assertFalse(metagram_checker("test", "testing"))

    def test_case_insensitivity(self):
        self.assertTrue(metagram_checker("Spin", "spit"))

    def test_two_empty_strings(self):
        self.assertFalse(metagram_checker("", ""))

    def test_one_empty_string(self):
        self.assertFalse(metagram_checker("word", ""))

    def test_words_with_special_characters(self):
        self.assertTrue(metagram_checker("c@t", "c#t"))

if __name__ == "__main__":
    unittest.main()