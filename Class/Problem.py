from Class.AbstractProblemClass import AbstractProblem
from abc import ABC, abstractmethod

class Problem(AbstractProblem):

    def __init__(self, initial_state, ordered_variables, variables_nature):
        super().__init__(initial_state, ordered_variables, variables_nature)

        self.initial_state = initial_state
        self.ordered_variables = ordered_variables
        self.variables_nature = variables_nature

    def equals(self, state_one, state_two):
        # Implementación del método Equals
        pass

    def transition_function(self, previus_state, variable_id, variable_value):
        # Implementación del método TransitionFunction
        pass

    def factibility_function(self, new_state, existed_state, variable_id, variable_value):
        # Implementación del método FactibilityFunction
        pass

    

