class Knapsack:

    def __init__(self, n_variables, variable_range, root_state_values):
        self.n_variables = n_variables
        self.variable_range = variable_range
        self.root_state = self.define_root_state(root_state_values)

    def is_this_state_factible(self, state) -> bool:
        raise NotImplementedError("is_this_state_factible function is not implemented")
    
    def get_next_state(self, state):
        raise NotImplementedError("get_next_state function is not implemented")

    
    def are_these_states_equal(self, states) -> bool:
        raise NotImplementedError("are_these_states_equal function is not implemented")


    def define_root_state(self, root_state_values):
        raise NotImplementedError("define_root_state function is not implemented")
        return State(root_state_values)

class State:
    
    def __init__(self, state_values):
        pass