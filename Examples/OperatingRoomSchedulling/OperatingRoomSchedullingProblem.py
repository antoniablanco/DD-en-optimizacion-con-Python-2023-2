from Class.Problems.AbstractProblemClass import AbstractProblem

class OperatingRoomSchedulling(AbstractProblem):

    def __init__(self, initial_state, variables):
        super().__init__(initial_state, variables)

    def equals(self, state_one, state_two):
        return state_one == state_two

    def transition_function(self, previus_state, variable_id, variable_value):
        is_feasible = True
        if variable_value in previus_state:
            is_feasible = False
        new_state = [i for i in previus_state]
        new_state.append(variable_value)
        return new_state, is_feasible