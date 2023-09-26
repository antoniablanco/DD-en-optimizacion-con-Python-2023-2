from Class.AbstractProblemClass import AbstractProblem
from abc import ABC, abstractmethod

class Problem(AbstractProblem):

    def __init__(self, initial_state, ordered_variables, variables_nature):
        super().__init__(initial_state, ordered_variables, variables_nature)

        self.initial_state = initial_state
        self.ordered_variables = ordered_variables
        self.variables_nature = variables_nature

    def are_these_states_equal(self, states) -> bool:
        pass

    def transition_function(self, previus_state, variable, value):
        # Implementación del método TransitionFunction
        pass

    def is_this_state_factible(self, state) -> bool:
        pass

    def get_next_state(self, state):
        pass

    def define_equals_function(self, costume_equals):
        setattr(self, 'are_these_states_equal', costume_equals)

    def define_transition_function(self, costume_transition_function):
        setattr(self, 'transition_function', costume_transition_function)

    def define_factibility_function(self, costume_factibility_function):
        setattr(self, 'is_this_state_factible', costume_factibility_function)

    def define_next_state_function(self, costume_next_state_function):
        setattr(self, 'get_next_state', costume_next_state_function)

    def define_state_class(self, costume_state_class):
        setattr(self, 'state_class', costume_state_class)
    

