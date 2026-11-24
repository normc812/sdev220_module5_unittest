import unittest

# Function to be tested
def add(a, b):
    return a + b

class TestMathOperations(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 6)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)

if __name__ == '__main__':
    unittest.main()
# 
# this tests adding positive and negative numbers:
# `2 + 3 == 6`: fails because the result is `5`.
# `-1 + -1 == -2`: passes.
#