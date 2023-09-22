import unittest
from knapsack import knapsack_function

class TestSum(unittest.TestCase):
    def test_knapsack(self):
        """
        Test that it can sum a list of fractions
        """
        result = knapsack_function()
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()