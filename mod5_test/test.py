# test.py

import unittest

from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

if __name__ == "__main__":
    unittest.main()
#    
# this code calls a unit test for the sum 
# function defined in the my_sum module. 
# It checks if the sum of a list of integers 
# [1, 2, 3] equals 6. If the test passes, 
# it confirms that the sum function works 
# correctly for this input.   
# if it returns an error, it indicates that there
# is an issue with the sum function definition.
# the last two lines allow the test to be run directly 
# from the command line.

    