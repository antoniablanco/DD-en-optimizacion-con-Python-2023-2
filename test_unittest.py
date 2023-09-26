import unittest
from knapsack import Knapsack, State

class TestKnapsackMethodsExistance(unittest.TestCase):
    
    def setUp(self):
        self.knapsack = Knapsack(n_variables=3, variable_range=(0, 1), root_state_values=[0, 0, 0])

    def test_is_this_state_factible_defined(self):
        self.assertTrue(hasattr(self.knapsack, "is_this_state_factible") and callable(self.knapsack.is_this_state_factible))

    def test_get_next_state_defined(self):
        self.assertTrue(hasattr(self.knapsack, "get_next_state") and callable(self.knapsack.get_next_state))

    def test_are_these_states_equal_defined(self):
        self.assertTrue(hasattr(self.knapsack, "are_these_states_equal") and callable(self.knapsack.are_these_states_equal))

class TestKnapsackMethods(unittest.TestCase):
    
    def setUp(self):
        self.knapsack = Knapsack(n_variables=3, variable_range=(0, 1), root_state_values=[0, 0, 0])

    def test_are_these_states_equal(self):
        state1 = State([0, 0, 0])
        state2 = State([0, 0, 0])
        self.assertTrue(self.knapsack.are_these_states_equal(state1, state2))
    
    def test_are_these_states_equal2(self):
        state1 = State([0, 0, 0])
        state2 = State([0, 0, 1])
        self.assertFalse(self.knapsack.are_these_states_equal(state1, state2))

    def test_get_next_state(self):
        state = State([0, 0, 0])
        self.assertEqual(self.knapsack.get_next_state(state), State([0, 0, 1]))

    def test_get_next_state2(self):
        state = State([0, 0, 1])
        self.assertEqual(self.knapsack.get_next_state(state), State([0, 1, 0]))

    def test_is_this_state_factible(self):
        state = State([0, 0, 0])
        self.assertTrue(self.knapsack.is_this_state_factible(state))
    
    def test_is_this_state_factible2(self):
        state = State([0, 0, 1])
        self.assertFalse(self.knapsack.is_this_state_factible(state))
        
        


if __name__ == '__main__':
    unittest.main()
