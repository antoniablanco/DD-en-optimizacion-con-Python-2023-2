from abc import ABC, abstractmethod

class AbstractProblem(ABC):

    def __init__(self, initial_state, variables):
        self.initial_state = initial_state
        self.ordered_variables = self.get_variables(variables)
        self.variables_domain = self.get_variables_domain(variables)
    
    def get_variables(self, variablesAndDomain):
        variables_ordenadas = []
        for var in variablesAndDomain:
            variables_ordenadas.append(var[0])
        return variables_ordenadas
    
    def get_variables_domain(self, variablesAndDomain):
        variables_domain = {}
        for var in variablesAndDomain:
            variables_domain[var[0]] = var[1]
        return variables_domain

    @abstractmethod
    def equals(self, state_one, state_two):
        pass

    @abstractmethod
    def transition_function(self, previus_state, variable_id, variable_value):
        pass

    