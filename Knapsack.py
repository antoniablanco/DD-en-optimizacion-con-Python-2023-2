from Class.AbstractProblemClass import AbstractProblem
from Class.MDD import MDD
from Class.MinMaxObjective import MinMaxFunction

class ProblemKnapsack(AbstractProblem):

    def __init__(self, initial_state, ordered_variables, variables_nature):
        super().__init__(initial_state, ordered_variables, variables_nature)

        self.initial_state = initial_state
        self.ordered_variables = ordered_variables
        self.variables_nature = variables_nature

    def equals(self, state_one, state_two):
        return state_one == state_two

    def transition_function(self, previus_state, variable_id, variable_value):
        lista_suma_variables = [3,3,4,6]
        new_state = int(previus_state[0])+lista_suma_variables[int(variable_id[2:])-1]*int(variable_value)
        return [new_state]

    def factibility_function(self, new_state, existed_state, variable_id, variable_value):
        return int(new_state[0]) <= 6


initial_state = [0]
ordered_variables = ['x_1','x_2','x_3','x_4']
variable_nature = [0, 1]

problem_instance = ProblemKnapsack(initial_state, ordered_variables, variable_nature)

mdd_instance = MDD(problem_instance)

mdd_instance.get_decision_diagram()
mdd_instance.get_reduce_decision_diagram()
#mdd_instance.print_decision_diagram()
#mdd_instance.print_reduce_decision_diagram()

mdd_instance.develop_solver(['binary', 'binary', 'binary', 'binary'],[-5, 1, 1, 17], 'min')
mdd_instance.solve_dd()
mdd_instance.export_margarita_file("test")

