import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
root_dir = os.path.abspath(os.path.join(parent_dir, os.pardir))
sys.path.append(root_dir)

from Class.DD import DD
from Class.ObjectiveFunction.ObjectiveFunction import ObjectiveFunction
from OperatingRoomSchedullingProblem import OperatingRoomSchedulling
from Class.ObjectiveFunction.SchedullingObjective import SchedullingObjective
import numpy as np

number_operations = 3

initial_state = []
variables = [(f'x_{i}', list(range(number_operations))) for i in range(number_operations)]

problem_instance = OperatingRoomSchedulling(initial_state, variables)

dd_instance = DD(problem_instance, verbose=False)
dd_instance.print_decision_diagram()
dd_instance.create_reduce_decision_diagram(verbose=False)
dd_instance.print_decision_diagram()
dd_instance.export_graph_file("test")

# Resolución del diagrama
objective_function_instance = ObjectiveFunction(dd_instance)
w = [[1, 1, 1], [[2, 1, 1], [2,2,5], [3,3,2]]]
schedulling_objective_instance = SchedullingObjective(w, 'min')
objective_function_instance.set_objective(schedulling_objective_instance)
objective_function_instance.solve_dd()
