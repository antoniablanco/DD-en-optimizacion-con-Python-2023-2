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
dd_instance.print_decision_diagram()
dd_instance.create_reduce_decision_diagram(v=False)
dd_instance.print_decision_diagram()
dd_instance.export_graph_file("test")

decision_diagram = dd_instance.get_decision_diagram_graph()