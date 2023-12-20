import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
root_dir = os.path.abspath(os.path.join(parent_dir, os.pardir))
sys.path.append(root_dir)

from Class.DD import DD
from Class.ObjectiveFunction.ObjectiveFunction import ObjectiveFunction, LinearObjective
from Exceptions.MyExceptions import SameVariables, MustBeIntegers, ConsistentDictionaryOfNeighbors
from IndependentSetProblem import ProblemIndependentSet

'''
El siguiente atributo fue implementado para obtener un independent set de un grafo
de forma que este sea general y no instanciado.
Para ello DictVecino debe se un diccionario de la forma: { variable_id: [vecinos] } donde
las variables id utilizadas deben ser las mismas que se entregan como key dentro de variables. 
Los vecinos deben ser una lista de enteros que referencias los nodos vecinos a la variable_id.
'''
# Atributos para crear Independent Set
DictVecinos = {'x_1': [2, 3], 'x_2': [1, 3, 4], 'x_3': [1, 2, 4], 'x_4': [2, 3, 5], 'x_5': [4, 6], 'x_6': [5]}
    
# Valores construcción abstract problem
initial_state = [1, 2, 3, 4, 5]
variables = [('x_1', [0, 1]), ('x_2', [0, 1]), ('x_3', [0, 1]), ('x_4', [0, 1]), ('x_5', [0, 1]), ('x_6', [0, 1])]

problem_instance = ProblemIndependentSet(initial_state, variables, DictVecinos)

dd_instance = DD(problem_instance, verbose=False)

dd_instance.print_decision_diagram()
dd_instance.create_reduce_decision_diagram(verbose=False)
dd_instance.print_decision_diagram()
dd_instance.export_graph_file("test2")

objective_function_instance = ObjectiveFunction(dd_instance)
linear_objective_instance = LinearObjective([1, 1, 1, 1, 1, 1], 'min')
objective_function_instance.set_objective(linear_objective_instance)
objective_function_instance.solve_dd()
print(objective_function_instance.get_time())




