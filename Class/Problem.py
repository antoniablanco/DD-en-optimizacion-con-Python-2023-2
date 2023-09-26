from Class.AbstractProblemClass import AbstractProblem
from abc import ABC, abstractmethod

class Problem(AbstractProblem):

    def __init__(self, initial_state, ordered_variables, variables_nature):
        super().__init__(initial_state, ordered_variables, variables_nature)

        self.initial_state = initial_state
        self.ordered_variables = ordered_variables
        self.variables_nature = variables_nature

    def equals(self, stateOne, stateTwo):
        # Implementación del método Equals
        pass

    def transition_function(self, previus_state, variable, value):
        # Implementación del método TransitionFunction
        pass

    def factibility_function(self, state):
        # Implementación del método FactibilityFunction
        pass

    def define_equals_function(self, costume_equals):
        setattr(self, 'equals', costume_equals)

    def define_transition_function(self, costume_transition_function):
        setattr(self, 'transition_function', costume_transition_function)

    def define_factibility_function(self, costume_factibility_function):
        setattr(self, 'factibility_function', costume_factibility_function)
    

