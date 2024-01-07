from Class.Problems.AbstractProblemClass import AbstractProblem
from Exceptions.MyExceptions import SameLenError

from Class.decorators.timer import timing_decorator

class SetCoveringProblem(AbstractProblem):

    @timing_decorator(enabled=False)
    def __init__(self, initial_state, variables, matrix_of_wheight, right_side_of_restrictions):
        super().__init__(initial_state, variables)

        self.matrix_of_wheight = matrix_of_wheight
        self.right_side_of_restrictions = right_side_of_restrictions

        self.check_atributes(variables, initial_state)

    def check_atributes(self, variables, initial_state):
        self.check_same_len_matrix_and_right_side(initial_state)
        self.check_same_len_rows_matrix_and_variables(variables)
    
    def check_same_len_matrix_and_right_side(self, initial_state):
        assert len(self.matrix_of_wheight) == len(self.right_side_of_restrictions), "matrix_of_wheight and right_side_of_restrictions must have the same length"
        assert len(initial_state) == len(self.right_side_of_restrictions) or len(initial_state) == 2*len(self.right_side_of_restrictions), "matrix_of_wheight and right_side_of_restrictions must have the same length"
    
    def check_same_len_rows_matrix_and_variables(self, variables):
        for row in range(len(self.matrix_of_wheight)):
            assert len(self.matrix_of_wheight[row]) == len(variables), "rows of matrix_of_wheight and right_side_of_restrictions must have the same length of variables"

    def equals(self, state_one, state_two):
        return set(state_one) == set(state_two)

    def transition_function(self, previus_state, variable_id, variable_value):
        isFeasible = True

        if int(variable_value) == 0:
            new_state = previus_state.copy()
            for row in previus_state:
                maximo = len(self.matrix_of_wheight[row-1]) - self.matrix_of_wheight[row-1][::-1].index(1) 
                if int(variable_id[2:]) >= maximo:
                    isFeasible = False 
        else:
            new_state = []
            for row in previus_state:
                if self.matrix_of_wheight[row-1][int(variable_id[2:])-1] != 1:
                    new_state.append(row)
        
        return new_state, isFeasible
    
    def get_priority_for_discard_node(self, state):
        pass
    
    def get_priority_for_merge_nodes(self, id_node, state):
        pass

    def merge_operator(self, state_one, state_two):
        pass