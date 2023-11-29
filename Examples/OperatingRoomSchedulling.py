import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)

from Class.DD import DD
from Class.ObjectiveFunction.ObjectiveFunction import ObjectiveFunction
from Class.Problems.OperatingRoomSchedullingProblem import OperatingRoomSchedulling
import numpy as np

number_operations = 4

initial_state = []
variables = [(f'x_{i}', list(range(number_operations))) for i in range(number_operations)]

problem_instance = OperatingRoomSchedulling(initial_state, variables)

dd_instance = DD(problem_instance, v=False)
#dd_instance.print_decision_diagram()
dd_instance.create_reduce_decision_diagram(v=False)
#dd_instance.print_decision_diagram()
dd_instance.export_graph_file("test")

decision_diagram = dd_instance.get_decision_diagram_graph()

# Resolución del diagrama
objective_function_instance = ObjectiveFunction(decision_diagram)

w = [[1.39, 2.12, 2.29, 2.1], [[0.58, 0.42, 0.58, 0.39], [0.66, 0.51, 0.61, 0.48], [0.6, 0.4, 0.46, 0.43], [0.66, 0.21, 0.54, 0.47]]]
objective_function_instance.develop_solver(w, 'min')
objective_function_instance.solve_dd()

w = [[1.91, 2.4, 2.23, 1.96], [[0.35, 0.48, 0.43, 0.36], [0.55, 0.41, 0.56, 0.4], [0.31, 0.53, 0.38, 0.47], [0.41, 0.31, 0.59, 0.38]]]
objective_function_instance.develop_solver(w, 'min')
objective_function_instance.solve_dd()