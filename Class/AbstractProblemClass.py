from abc import ABC, abstractmethod

class AbstractProblem(ABC):

    def __init__(self, inicial_state, ordered_variables, variable_nature):
        pass

    @abstractmethod
    def equals(self, state_one, state_two):
        pass

    @abstractmethod
    def transition_function(self, previus_state, variable_id, variable_value):
        pass

    @abstractmethod
    def factibility_function(self, new_state, existed_state, variable_id, variable_value):
        pass
    