from Test import IndependentSet_test, Knapsack_test
import unittest

if __name__ == '__main__':
    suite = unittest.TestSuite()

    suite.addTests(unittest.TestLoader().loadTestsFromModule(IndependentSet_test))
    suite.addTests(unittest.TestLoader().loadTestsFromModule(Knapsack_test))

    unittest.TextTestRunner().run(suite)