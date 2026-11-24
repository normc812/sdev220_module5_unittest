import unittest

def categorize_by_age(age):
    if 0 <= age <= 9:
        return "Child"
    elif 9 < age <= 18:
        return "Adolescent"
    elif 18 < age <= 65:
        return "Adult"
    elif 65 < age <= 150:
        return "Golden age"
    else:
        return f"Invalid age: {age}"
#


# from age import categorize_by_age

class TestCategorizeByAge(unittest.TestCase):
    def test_child(self):
        self.assertEqual(categorize_by_age(5), "Child")

    def test_adolescent(self):
        self.assertEqual(categorize_by_age(15), "Adolescent")

    def test_adult(self):
        self.assertEqual(categorize_by_age(30), "Adult")

    def test_golden_age(self):
        self.assertEqual(categorize_by_age(70), "Golden age")

    def test_negative_age(self):
        self.assertEqual(categorize_by_age(-1), "Invalid age: -1")

    def test_too_old(self):
        self.assertEqual(categorize_by_age(151), "Invalid age: 151")    

    def test_boundary_child_adolescent(self):
        self.assertEqual(categorize_by_age(9), "Child")
        self.assertEqual(categorize_by_age(10), "Adolescent")

    def test_boundary_adolescent_adult(self):
        self.assertEqual(categorize_by_age(18), "Adolescent")
        self.assertEqual(categorize_by_age(19), "Adult")

    def test_boundary_adult_golden_age(self):
        self.assertEqual(categorize_by_age(65), "Adult")
        self.assertEqual(categorize_by_age(66), "Golden age")

#if __name__ == '__main__':
    #unittest.main()     
# ...

if __name__ == "__main__":
    unittest.main(verbosity=2)#    verbosity=2 provides more 
    # detailed output for each test case, 
  
# This code tests whether `categorize_by_age()` correctly labels ages 
# as Child, Adolescent, Adult, or Golden age.

# It checks typical ages, invalid ages (`-1` and `151`), 
# and category boundaries such as `9/10`, `18/19`, and `65/66`.

# All 9 tests should pass. `verbosity=2` 
# displays each test’s name and result.   