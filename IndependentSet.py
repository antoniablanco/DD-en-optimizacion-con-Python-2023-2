from Class.AbstractProblemClass import AbstractProblem
from Class.MDD import MDD

class ProblemIndependentSet(AbstractProblem):

    def __init__(self, initial_state, ordered_variables, variables_nature):
        super().__init__(initial_state, ordered_variables, variables_nature)

        self.initial_state = initial_state
        self.ordered_variables = ordered_variables
        self.variables_nature = variables_nature

    def equals(self, state_one, state_two):
        return set(state_one) == set(state_two)

    def transition_function(self, previus_state, variable_id, variable_value):
        DictVecinos = {'x_1':[2,3],'x_2':[1,3,4],'x_3':[1,2,4],'x_4':[2,3,5], 'x_5':[4]}
        if int(variable_value) == 0 and int(variable_id[2:]) in previus_state:
            new_state = previus_state.copy()
            new_state.remove(int(variable_id[2:]))
        elif int(variable_value) == 1 and int(variable_id[2:]) in previus_state:
            new_state = previus_state.copy()
            new_state.remove(int(variable_id[2:]))
            for vecino in DictVecinos[variable_id]:
                if vecino in new_state:
                    new_state.remove(vecino)
        else:
            new_state = previus_state.copy()
        
        return new_state

    def factibility_function(self, new_state, existed_state, variable_id, variable_value):
        return (int(variable_value) == 1 and int(variable_id[2:]) in existed_state) or (int(variable_value) == 0)

    
initial_state = [1,2,3,4,5]
ordered_variables = ['x_1','x_2','x_3','x_4', 'x_5']
variable_nature = [0, 1]

problem_instance = ProblemIndependentSet(initial_state, ordered_variables, variable_nature)

mdd_instance = MDD(problem_instance)

mdd_instance.get_decision_diagram()
mdd_instance.get_reduce_decision_diagram()
mdd_instance.develop_solver(['binary', 'binary', 'binary', 'binary', 'binary'], ['+', '+', '+', '+', '+'], [1, 1, 1, 1, 1], 'max')
mdd_instance.solve_dd()
file_name = mdd_instance.get_margarita_file("test2")

mdd_instance.print_decision_diagram()
mdd_instance.print_reduce_decision_diagram()



