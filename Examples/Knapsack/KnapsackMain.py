import os
import sys

print("------------------")
print(sys.path)

current_dir = os.path.dirname(os.path.abspath(__file__))

parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

root_dir = os.path.abspath(os.path.join(parent_dir, os.pardir))
sys.path.append(root_dir)

from Class.DD import DD 
from Class.ObjectiveFunction.ObjectiveFunction import ObjectiveFunction
from Exceptions.MyExceptions import SameLenError
from KnapsackProblem import ProblemKnapsack

'''
Los siguientes 2 atributos fueron agregados solo para el tipo de problema de Knapsack, 
de forma que este sea general y no instanciado.
Para ello es necesario que el largo de cada row dentro de matrix_of_wheight sea
igual al de right_side_of_restrictions, al de variables y initial_state.
Deben ser valores enteros.
'''

# Valores construcción knapsack
matrix_of_wheight = [[3, 3, 4, 6], [2, 2, 1, 5], [4, 2, 1, 3]]
right_side_of_restrictions = [6, 5, 8]

# Valores construcción abstract problem
initial_state = [0, 0, 0]
variables = [('x_1', [0, 1]), ('x_2', [0, 1, 2]), ('x_3', [0, 1]), ('x_4', [0, 1])]

problem_instance = ProblemKnapsack(initial_state, variables, matrix_of_wheight, right_side_of_restrictions)

dd_instance = DD(problem_instance, verbose=False)

# Construcción del diagrama de decisión
dd_instance.print_decision_diagram()
dd_instance.create_reduce_decision_diagram(verbose=False)
dd_instance.print_decision_diagram()
dd_instance.export_graph_file("test")

# Resolución del diagrama
objective_function_instance = ObjectiveFunction(dd_instance)
objective_function_instance.develop_solver([-5, 1, 18, 17], 'max')
objective_function_instance.solve_dd()

