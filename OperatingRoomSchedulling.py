from Class.AbstractProblemClass import AbstractProblem
from Class.DD import DD
from Class.ObjectiveFunction import ObjectiveFunction
import numpy as np


class OperatingRoomSchedulling(AbstractProblem):

    def __init__(self, initial_state, variables):
        super().__init__(initial_state, variables)

    def equals(self, state_one, state_two):
        return state_one == state_two

    def transition_function(self, previus_state, variable_id, variable_value):
        is_feasible = True
        if variable_value in previus_state:
            is_feasible = False
        new_state = [i for i in previus_state]
        new_state.append(variable_value)
        return new_state, is_feasible

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
