import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)

from Class.Problems.AbstractProblemClass import AbstractProblem
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
        assert dict(variables).keys() == self.dict_node_neighbors.keys(), "Variables must be the same between dictionaries"
    
    def check_neighbors_must_be_integers(self):
        for key in self.dict_node_neighbors.keys():
            for value in self.dict_node_neighbors.get(key, []):
                assert isinstance(value, int), "Values must be integers"
    
    def check_consistent_dictionary_of_neighbors(self):
        for key in self.dict_node_neighbors.keys():
            for value in self.dict_node_neighbors.get(key, []):
                assert int(key[2:]) in self.dict_node_neighbors.get("x_"+str(value), []), "Dictionary of neighbors must be consistent"

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

    def get_sort_value(self, state):
        return len(state)
    
    def sort_key_nodes_to_merge(self, id_node):
        return int(id_node)

    def merge_operator(self, state_one, state_two):
        return list(set((state_one + state_two)))