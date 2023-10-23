from Class.AbstractProblemClass import AbstractProblem
from Class.MDD import MDD
from Class.MinMaxObjective import MinMaxFunction


class ProblemKnapsack(AbstractProblem):

    def __init__(self, initial_state, variables):
        super().__init__(initial_state, variables)

    def equals(self, state_one, state_two):
        return state_one == state_two

    def transition_function(self, previus_state, variable_id, variable_value):
        lista_suma_variables = [3, 3, 4, 6]
        new_state = [int(previus_state[0])+lista_suma_variables[int(variable_id[2:])-1]*int(variable_value)]

        flag = int(new_state[0]) <= 6
        return new_state, flag


initial_state = [0]
variables = [['x_1', [0, 1]], ['x_2', [0, 1]], ['x_3', [0, 1]], ['x_4', [0, 1]]]

problem_instance = ProblemKnapsack(initial_state, variables)

mdd_instance = MDD(problem_instance)

mdd_instance.print_decision_diagram()
mdd_instance.create_reduce_decision_diagram()
mdd_instance.print_decision_diagram()

mdd_instance.develop_solver(['binary', 'binary', 'binary', 'binary'],[-5, 1, 1, 17], 'min')
mdd_instance.solve_dd()
mdd_instance.export_margarita_file("test")

