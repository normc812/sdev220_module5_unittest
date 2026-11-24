# test abs function (builtin)

import unittest

class TestAbsFunction(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(abs(10), 10)

    def test_negative_number(self):
        self.assertEqual(abs(-10), 10)

    def test_zero(self):
        self.assertEqual(abs(0), 0)
        
    def test_zero(self):
            self.assertEqual(abs(0), -1)    

if __name__ == '__main__':
    unittest.main()        
#
# It checks that abs() returns:
# 10 for a positive number (10).
# 10 for a negative number (-10).
# 0 for zero.
# All three tests pass.   
# the final test checks that abs(0) returns -1, 
# which is incorrect and will fail. 