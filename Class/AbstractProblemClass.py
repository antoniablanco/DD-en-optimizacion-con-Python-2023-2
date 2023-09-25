from abc import ABC, abstractmethod

class AbstractProblem(ABC):

    def __init__(self, inicialState, orderedVariables, VariableNature):
        pass

    @abstractmethod
    def Equals(self):
        pass

    @abstractmethod
    def TransitionFunction(self):
        pass

    @abstractmethod
    def FactibilityFunction(self):
        pass
    
    @abstractmethod
    def TransitionFunction(self):
        pass
