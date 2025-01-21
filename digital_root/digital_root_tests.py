import unittest
from digital_root_calculator import digital_root

class TestDigitalRoot(unittest.TestCase):
    def test_single_digit(self):
        self.assertEqual(digital_root(0), 0)
        self.assertEqual(digital_root(5), 5)
        self.assertEqual(digital_root(9), 9)

    def test_multiple_digits(self):
        self.assertEqual(digital_root(10), 1)  
        self.assertEqual(digital_root(354), 3)  
        self.assertEqual(digital_root(9876), 3)  
        
    def test_large_numbers(self):
        self.assertEqual(digital_root(123456789), 9)
        self.assertEqual(digital_root(987654321), 9)

    def test_edge_cases(self):
        self.assertEqual(digital_root(1), 1)
        self.assertEqual(digital_root(11), 2)
        self.assertEqual(digital_root(1000), 1)

if __name__ == '__main__':
    unittest.main()