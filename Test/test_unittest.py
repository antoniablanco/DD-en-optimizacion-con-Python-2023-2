import unittest
from Class.Problem import Problem
from public.classes import State
from public.functions import custom_equals, custom_transition_function, custom_factibility_function


class TestKnapsackMethodsExistance(unittest.TestCase):
    
    def setUp(self):
        initial_state = [0]
        ordered_variables = ['x_1','x_2','x_3','x_4']
        variable_nature = [0, 1]

        self.problem = Problem(initial_state, ordered_variables, variable_nature)
        self.problem.define_equals_function(custom_equals)
        self.problem.define_transition_function(custom_transition_function)
        self.problem.define_factibility_function(custom_factibility_function)
        self.problem.define_next_state_function(custom_transition_function)
        self.problem.define_state_class(State)

    def test_is_this_state_factible_defined(self):
        self.assertTrue(hasattr(self.problem, "is_this_state_factible") and callable(self.problem.is_this_state_factible))

    def test_get_next_state_defined(self):
        self.assertTrue(hasattr(self.problem, "get_next_state") and callable(self.problem.get_next_state))

    def test_are_these_states_equal_defined(self):
        self.assertTrue(hasattr(self.problem, "are_these_states_equal") and callable(self.problem.are_these_states_equal))

class TestKnapsackMethods(unittest.TestCase):
    
    def setUp(self):
        initial_state = [0]
        ordered_variables = ['x_1','x_2','x_3','x_4']
        variable_nature = [0, 1]

        self.problem = Problem(initial_state, ordered_variables, variable_nature)
        self.problem.define_equals_function(custom_equals)
        self.problem.define_transition_function(custom_transition_function)
        self.problem.define_factibility_function(custom_factibility_function)
        # self.problem.define_next_state_function(custom_transition_function)
        self.problem.define_state_class(State)

    def test_are_these_states_equal(self):
        pass
        state1 = State([0, 0, 0])
        state2 = State([0, 0, 0])
        self.assertTrue(self.problem.are_these_states_equal(state1.state_values, state2.state_values))
    
    def test_are_these_states_equal2(self):
        state1 = State([0, 0, 0])
        state2 = State([0, 0, 1])
        self.assertFalse(self.problem.are_these_states_equal(state1, state2))

    # def test_get_next_state(self):
    #     state = State([0, 0, 0])
    #     self.assertEqual(self.problem.get_next_state(state), State([0, 0, 1]))

    # def test_get_next_state2(self):
    #     present_state = State([0, 0, 1])
    #     next_state = State([0, 1, 0])
    #     self.assertEqual(self.problem.get_next_state(present_state), next_state))

    def test_is_this_state_factible(self):
        state = State([0, 0, 0])
        self.assertTrue(self.problem.is_this_state_factible(state))
    
    def test_is_this_state_factible2(self):
        state = State([6, 5, 3])
        self.assertFalse(self.problem.is_this_state_factible(state))
        
        


if __name__ == '__main__':
    unittest.main()
