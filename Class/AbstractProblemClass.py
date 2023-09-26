from abc import ABC, abstractmethod

class AbstractProblem(ABC):

    def __init__(self, inicial_state, ordered_variables, variable_nature):
        pass

    @abstractmethod
    def equals(self):
        pass

    @abstractmethod
    def transition_function(self):
        pass

    @abstractmethod
    def factibility_function(self):
        pass
    
    @abstractmethod
    def transition_function(self):
        pass
