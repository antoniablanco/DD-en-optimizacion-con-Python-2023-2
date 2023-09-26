from abc import ABC, abstractmethod

class AbstractProblem(ABC):

    def __init__(self, inicial_state, ordered_variables, variable_nature):
        pass

    @abstractmethod
    def are_these_states_equal(self, states) -> bool:
        pass

    @abstractmethod
    def transition_function(self):
        pass

    @abstractmethod
    def is_this_state_factible(self, state) -> bool:
        pass

    @abstractmethod
    def get_next_state(self, state):
        pass

