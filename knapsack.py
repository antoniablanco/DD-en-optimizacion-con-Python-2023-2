from Class.AbstractProblemClass import AbstractProblem
from Class.DD import DD
from Class.ObjectiveFunction import ObjectiveFunction


class ProblemKnapsack(AbstractProblem):

    def __init__(self, initial_state, variables):
        super().__init__(initial_state, variables)

    def equals(self, state_one, state_two):
        return state_one == state_two

    def transition_function(self, previus_state, variable_id, variable_value):
        lista_suma_variables = [3, 3, 4, 6]
        new_state = [int(previus_state[0])+lista_suma_variables[int(variable_id[2:])-1]*int(variable_value)]

        isFeasible = int(new_state[0]) <= 6
        return new_state, isFeasible


initial_state = [0]
variables = [('x_1', [0, 1]), ('x_2', [0, 1]), ('x_3', [0, 1]), ('x_4', [0, 1])]

problem_instance = ProblemKnapsack(initial_state, variables)

dd_instance = DD(problem_instance, v=False)

# Construcción del diagrama de decisión
dd_instance.print_decision_diagram()
dd_instance.create_reduce_decision_diagram(v=False)
dd_instance.print_decision_diagram()
dd_instance.export_graph_file("test")

decision_diagram = dd_instance.get_decision_diagram_graph()


# Resolución del diagrama
objective_function_instance = ObjectiveFunction(decision_diagram)
objective_function_instance.develop_solver([-5, 1, 18, 17], 'max')
objective_function_instance.solve_dd()

