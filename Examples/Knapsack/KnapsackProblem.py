from Class.Problems.AbstractProblemClass import AbstractProblem
from Exceptions.MyExceptions import SameLenError

from Class.decorators.timer import timing_decorator

class ProblemKnapsack(AbstractProblem):

    @timing_decorator(enabled=False)
    def __init__(self, initial_state, variables, list_of_wheight_for_restrictions, right_side_of_restrictions):
        super().__init__(initial_state, variables)

        self.list_of_wheight_for_restrictions = list_of_wheight_for_restrictions
        self.right_side_of_restrictions = right_side_of_restrictions

        self.check_atributes(variables, initial_state)

    def check_atributes(self, variables, initial_state):
        self.check_same_len_matrix_and_right_side(initial_state)
        self.check_same_len_rows_matrix_and_variables(variables)
    
    def check_same_len_matrix_and_right_side(self, initial_state):
        assert len(self.list_of_wheight_for_restrictions) == len(self.right_side_of_restrictions), "matrix_of_wheight and right_side_of_restrictions must have the same length"
        assert len(initial_state) == len(self.right_side_of_restrictions) or len(initial_state) == 2*len(self.right_side_of_restrictions), "matrix_of_wheight and right_side_of_restrictions must have the same length"
    
    def check_same_len_rows_matrix_and_variables(self, variables):
        for row in range(len(self.list_of_wheight_for_restrictions)):
            assert len(self.list_of_wheight_for_restrictions[row]) == len(variables), "rows of matrix_of_wheight and right_side_of_restrictions must have the same length of variables"

    def equals(self, state_one, state_two):
        return state_one == state_two

    def transition_function(self, previus_state, variable_id, variable_value):
        isFeasible = True
        state = []
        for row in range(len(self.list_of_wheight_for_restrictions)):
            lista_suma_variables = self.list_of_wheight_for_restrictions[row]
            new_state = int(previus_state[row][0])+lista_suma_variables[int(variable_id[2:])-1]*int(variable_value)
            state.append([new_state, new_state])

            isFeasible_this_row = int(state[row][0]) <= self.right_side_of_restrictions[row]
            isFeasible = isFeasible and isFeasible_this_row
        return state, isFeasible
    
    def get_priority_for_discard_node(self, state):
        total = 0
        for i in range(len(state)):
            total += state[i][0]
        return -total
    
    def get_priority_for_merge_nodes(self, id_node, state):
        if state[0][0] != state[0][1]:
            return -500
        return -int(id_node)

    def merge_operator(self, state_one, state_two):
        state = []
        for i in range(len(state_one)):
            state.append([state_one[i][0], state_two[i][1]])
        return state

