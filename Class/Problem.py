from Class.AbstractProblemClass import AbstractProblem
from abc import ABC, abstractmethod

class Problem(AbstractProblem):

    def __init__(self, initialState, orderedVariables, VariableNature):
        # Llamar al constructor de la clase base
        super().__init__(initialState, orderedVariables, VariableNature)

        self.initialState = initialState
        self.orderedVariables = orderedVariables
        self.VariableNature = VariableNature

    def Equals(self, stateOne, stateTwo):
        # Implementación del método Equals
        pass

    def TransitionFunction(self):
        # Implementación del método TransitionFunction
        pass

    def FactibilityFunction(self, state):
        # Implementación del método FactibilityFunction
        pass

    def DefineEqualsFunction(self, Equals):
        setattr(self, 'Equals', Equals)

    def DefineTransitionFunction(self, TransitionFunction):
        setattr(self, 'TransitionFunction', TransitionFunction)

    def DefineFactibilityFunction(self, FactibilityFunction):
        setattr(self, 'FactibilityFunction', FactibilityFunction)
    

