from Class.AbstractProblemClass import AbstractProblem
from Class.DD import DD
from Class.ObjectiveFunction import ObjectiveFunction 
from Exceptions.MyExceptions import SameVariables, MustBeIntegers, ConsistentDictionaryOfNeighbors


class ProblemIndependentSet(AbstractProblem):

    def __init__(self, initial_state, variables, dict_node_neighbors):
        super().__init__(initial_state, variables)
        self.dict_node_neighbors = dict_node_neighbors

        self.check_atributes(variables)

    def check_atributes(self, variables):
        self.check_same_variables(variables)
        self.check_neighbors_must_be_integers()
        self.check_consistent_dictionary_of_neighbors()

    def check_same_variables(self, variables):
        if dict(variables).keys() != self.dict_node_neighbors.keys():
            raise SameVariables("Variables must be the same between dictionaries")
    
    def check_neighbors_must_be_integers(self):
        for key in self.dict_node_neighbors.keys():
            for value in self.dict_node_neighbors.get(key, []):
                if not isinstance(value, int):
                    raise MustBeIntegers("Values must be integers")
    
    def check_consistent_dictionary_of_neighbors(self):
        for key in self.dict_node_neighbors.keys():
            for value in self.dict_node_neighbors.get(key, []):
                if int(key[2:]) not in self.dict_node_neighbors.get("x_"+str(value), []):
                    raise ConsistentDictionaryOfNeighbors("Dictionary of neighbors must be consistent")

    def equals(self, state_one, state_two):
        return set(state_one) == set(state_two)

    def transition_function(self, previus_state, variable_id, variable_value):
        if int(variable_value) == 0 and int(variable_id[2:]) in previus_state:
            new_state = previus_state.copy()
            new_state.remove(int(variable_id[2:]))
        elif int(variable_value) == 1 and int(variable_id[2:]) in previus_state:
            new_state = previus_state.copy()
            new_state.remove(int(variable_id[2:]))
            for vecino in self.dict_node_neighbors[variable_id]:
                if vecino in new_state:
                    new_state.remove(vecino)
        else:
            new_state = previus_state.copy()
        
        isFeasible = (int(variable_value) == 1 and int(variable_id[2:]) in previus_state) or (int(variable_value) == 0)
        return new_state, isFeasible

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

dd_instance = DD(problem_instance, v=False)

dd_instance.print_decision_diagram()
dd_instance.create_reduce_decision_diagram(v=False)
dd_instance.print_decision_diagram()
dd_instance.export_graph_file("test2")

decision_diagram = dd_instance.get_decision_diagram_graph()

objective_function_instance = ObjectiveFunction(decision_diagram)
objective_function_instance.develop_solver([1, 1, 1, 1, 1], 'min')
objective_function_instance.solve_dd()




