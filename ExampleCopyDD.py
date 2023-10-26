from Class.AbstractProblemClass import AbstractProblem
from Class.DD import DD
from Class.Node import Node
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

dd_instance.create_reduce_decision_diagram(v=False)

decision_diagram = dd_instance.get_decision_diagram_graph()
copy_decision_diagram = dd_instance.get_decision_diagram_graph_copy()


''' Ejemplo de que copy funciona bien, se obtiene el original y una copia.
a la copia se le agrega un nodo y se compara el último nodo de ambos. 
Pudiendo notar que estos no son iguales'''

print("")
print("Nodo original inicial", decision_diagram.nodes[-1])
print("Nodo copiado inicial", copy_decision_diagram.nodes[-1])

node_root = Node(0, initial_state)
copy_decision_diagram.add_node(node_root)

print("Nodo original final", decision_diagram.nodes[-1])
print("Nodo copiado final", copy_decision_diagram.nodes[-1])
