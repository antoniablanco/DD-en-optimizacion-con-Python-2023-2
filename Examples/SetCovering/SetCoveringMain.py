import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))

parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

root_dir = os.path.abspath(os.path.join(parent_dir, os.pardir))
sys.path.append(root_dir)

from Class.DD import DD 
from Class.ObjectiveFunction.ObjectiveFunction import ObjectiveFunction, LinearObjective
from SetCoveringProblem import SetCoveringProblem

'''
Ejemplo de Set covering problem
'''

# Valores construcción abstract problem
initial_state = [1, 2, 3]
variables = [('x_1', [0, 1]), ('x_2', [0, 1]), ('x_3', [0, 1]), ('x_4', [0, 1]), ('x_5', [0, 1]), ('x_6', [0, 1])]

# Valores construcción Set covering problem
matrix_of_wheight = [[1, 1, 1, 0, 0, 0],
                     [1, 0, 0, 1, 1, 0],
                     [0, 1, 0, 1, 0, 1]]

right_side_of_restrictions = [1, 1, 1]

problem_instance = SetCoveringProblem(initial_state, variables, matrix_of_wheight, right_side_of_restrictions)

dd_instance = DD(problem_instance, verbose=False)

# Construcción del los diagramas de decisión
#dd_instance.print_decision_diagram()
#dd_instance.create_reduce_decision_diagram(verbose=False)
#dd_instance.print_decision_diagram()
dd_instance.create_restricted_decision_diagram(verbose=False, max_width=3)
dd_instance.print_decision_diagram()
#dd_instance.create_relaxed_decision_diagram(verbose=False, max_width=3)
#dd_instance.print_decision_diagram()
dd_instance.export_graph_file("file")

# Resolución del diagrama
objective_function_instance = ObjectiveFunction(dd_instance)
linear_objective_instance = LinearObjective([2, 1, 4, 3, 4, 3], 'min')
objective_function_instance.set_objective(linear_objective_instance)
objective_function_instance.solve_dd()