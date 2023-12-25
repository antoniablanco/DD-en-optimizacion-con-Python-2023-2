import io
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)
 
import unittest
from unittest.mock import patch
from Class.Problems.AbstractProblemClass import AbstractProblem
from Class.DD import DD
from Class.ObjectiveFunction.ObjectiveFunction import ObjectiveFunction, LinearObjective
from contextlib import contextmanager
import dd_controlled_generators.DDIndependentSet as DDIndependentSet
import dd_controlled_generators.RestrictedDDIndependentSet as RestrictedDDIndependentSet
import dd_controlled_generators.DiferentOrderedRestrictedDDIndependentSet as DiferentOrderedRestrictedDDIndependentSet
import dd_controlled_generators.RelaxedDDIndependentSet as RelaxedDDIndependentSet

@contextmanager
def assertNoRaise():
    try:
        yield
    except Exception as e:
        raise AssertionError(f"Se generó una excepción: {e}")


class ProblemIndependentSetTest(unittest.TestCase):
    def setUp(self):
        class ProblemIndependentSet(AbstractProblem):

            def __init__(self, initial_state, variables):
                super().__init__(initial_state, variables)

            def equals(self, state_one, state_two):
                return set(state_one) == set(state_two)

            def transition_function(self, previus_state, variable_id, variable_value):
                DictVecinos = {'x_1': [2, 3], 'x_2': [1, 3, 4], 'x_3': [1, 2, 4], 'x_4': [2, 3, 5], 'x_5': [4]}
                if int(variable_value) == 0 and int(variable_id[2:]) in previus_state:
                    new_state = previus_state.copy()
                    new_state.remove(int(variable_id[2:]))
                elif int(variable_value) == 1 and int(variable_id[2:]) in previus_state:
                    new_state = previus_state.copy()
                    new_state.remove(int(variable_id[2:]))
                    for vecino in DictVecinos[variable_id]:
                        if vecino in new_state:
                            new_state.remove(vecino)
                else:
                    new_state = previus_state.copy()
                
                isFeasible = (int(variable_value) == 1 and int(variable_id[2:]) in previus_state) or (int(variable_value) == 0)
                return new_state, isFeasible
            
            def sort_key(self, state):
                return len(state)
            
            def sort_key_nodes_to_merge(self, id_node):
                return int(id_node)

            def merge_operator(self, state_one, state_two):
                return list(set((state_one + state_two)))
    
        independent_set_initial_state = [1, 2, 3, 4, 5]
        independent_set_variables = [('x_1', [0, 1]), ('x_2', [0, 1]), ('x_3', [0, 1]), ('x_4', [0, 1]), ('x_5', [0, 1])]
        self.independent_set_instance = ProblemIndependentSet(independent_set_initial_state, independent_set_variables)
        self.dd_independent_instance = DD(self.independent_set_instance, verbose=False)
 
    def test_ordered_variables(self):
        ordered_variables_test = ['x_1', 'x_2', 'x_3', 'x_4', 'x_5']
        self.assertEqual(self.independent_set_instance.ordered_variables, ordered_variables_test)
    
    def test_variables_domain(self):
        variables_domain_test = {'x_1': [0, 1], 'x_2': [0, 1], 'x_3': [0, 1], 'x_4': [0, 1], 'x_5': [0, 1]}
        self.assertEqual(self.independent_set_instance.variables_domain, variables_domain_test)

    def test_is_dd_created(self):
        dd_independent_instance = DD(self.independent_set_instance, verbose=True)
        self.assertIsNotNone(dd_independent_instance.graph_DD)
    
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_verbose_create_dd(self, mock_stdout):
        dd_independent_instance = DD(self.independent_set_instance, verbose=True)

        file_path = os.path.join('Test', 'test_prints', 'createDDIndependentSet.txt')
        
        with open(file_path, "r") as file:
            expected_output = file.read()

        actual_output = mock_stdout.getvalue()

        self.assertEqual(actual_output.strip(), expected_output.strip())
    
    def test_create_dd_graph_equal(self):
        dd_independent_instance = DD(self.independent_set_instance, verbose=False)
        resultado = dd_independent_instance.graph_DD == DDIndependentSet.graph
        self.assertTrue(resultado)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_verbose_create_reduce_dd(self, mock_stdout):
        dd_independent_set_instance = DD(self.independent_set_instance, verbose=False)
        dd_independent_set_instance.create_reduce_decision_diagram(verbose=True)

        file_path = os.path.join('Test', 'test_prints', 'createReduceDDIndependentSet.txt')
        
        with open(file_path, "r") as file:
            expected_output = file.read()

        actual_output = mock_stdout.getvalue()
        print(actual_output.strip())

        self.assertEqual(actual_output.strip(), expected_output.strip())
    
    def test_create_reduce_dd_graph_equal(self):
        dd_independent_set_instance = DD(self.independent_set_instance, verbose=False)
        dd_independent_set_instance.create_reduce_decision_diagram(verbose=False)
        resultado = dd_independent_set_instance.graph_DD == DDIndependentSet.graph
        self.assertTrue(resultado)
    
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_verbose_create_restricted_dd(self, mock_stdout):
        dd_independent_set_instance = DD(self.independent_set_instance, verbose=False)
        dd_independent_set_instance.create_restricted_decision_diagram(verbose=True, max_width=2)

        file_path = os.path.join('Test', 'test_prints', 'createRestrictedDDIndependentSet.txt')
        
        with open(file_path, "r") as file:
            expected_output = file.read()

        actual_output = mock_stdout.getvalue()
        print(actual_output.strip())

        self.assertEqual(actual_output.strip(), expected_output.strip())

    def test_create_restricted_dd_graph_equal(self):
        dd_independent_set_instance = DD(self.independent_set_instance, verbose=False)
        dd_independent_set_instance.create_restricted_decision_diagram(verbose=False, max_width=2)
        resultado = dd_independent_set_instance.graph_DD == RestrictedDDIndependentSet.graph

        self.assertTrue(resultado)
    
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_verbose_create_relaxed_dd(self, mock_stdout):
        dd_independent_set_instance = DD(self.independent_set_instance, verbose=False)
        dd_independent_set_instance.create_relaxed_decision_diagram(verbose=True, max_width=2)

        file_path = os.path.join('Test', 'test_prints', 'createRelaxedDDIndependentSet.txt')
        
        with open(file_path, "r") as file:
            expected_output = file.read()

        actual_output = mock_stdout.getvalue()
        print(actual_output.strip())

        self.assertEqual(actual_output.strip(), expected_output.strip())

    def test_create_relaxed_dd_graph_equal(self):
        dd_independent_set_instance = DD(self.independent_set_instance, verbose=False)
        dd_independent_set_instance.create_relaxed_decision_diagram(verbose=False, max_width=2)
        resultado = dd_independent_set_instance.graph_DD == RelaxedDDIndependentSet.graph

        self.assertTrue(resultado)
    
    def test_compare_two_diferent_ordered_graphs(self):
        dd_independent_set_instance = DD(self.independent_set_instance, verbose=False)
        dd_independent_set_instance.create_restricted_decision_diagram(verbose=False, max_width=2)
        resultado = dd_independent_set_instance.graph_DD == DiferentOrderedRestrictedDDIndependentSet.graph

        self.assertTrue(resultado)

    def test_get_dd_graph(self):
        dd_independent_set_instance = DD(self.independent_set_instance, verbose=False)
        self.assertIsNotNone(dd_independent_set_instance.get_decision_diagram_graph())
    
    @patch('matplotlib.pyplot.show')
    def test_print_dd_graph(self, mock_show):
        dd_independent_set_instance = DD(self.independent_set_instance, verbose=False)

        with assertNoRaise():
            dd_independent_set_instance.print_decision_diagram()
            mock_show.assert_called_once()
    
    def test_get_copy(self):
        dd_independent_set_instance = DD(self.independent_set_instance, verbose=False)
        self.assertIsNot(dd_independent_set_instance.graph_DD, dd_independent_set_instance.get_decision_diagram_graph_copy)

    def test_get_DDBuilder_time(self):
        dd_independent_set_instance = DD(self.independent_set_instance, verbose=False)
        self.assertTrue(dd_independent_set_instance.dd_builder_time > 0)
    
    def test_get_ReduceDDBuilder_time(self):
        dd_independent_set_instance = DD(self.independent_set_instance, verbose=False)
        dd_independent_set_instance.create_reduce_decision_diagram(verbose=False)
        self.assertTrue(dd_independent_set_instance.reduce_dd_builder_time > 0)
    
    def test_get_RestrictedDDBuilder_time(self):
        dd_independent_set_instance = DD(self.independent_set_instance, verbose=False)
        dd_independent_set_instance.create_restricted_decision_diagram(verbose=False)
        self.assertTrue(dd_independent_set_instance.restricted_dd_builder_time > 0)
    
    def test_get_RelaxedDDBuilder_time(self):
        dd_independent_set_instance = DD(self.independent_set_instance, verbose=False)
        dd_independent_set_instance.create_relaxed_decision_diagram(verbose=False)
        self.assertTrue(dd_independent_set_instance.relaxed_dd_builder_time > 0)
    
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_solution_for_DD(self, mock_stdout):
        dd_independent_set_instance = DD(self.independent_set_instance, verbose=False)

        objective_function_instance = ObjectiveFunction(dd_independent_set_instance)
        linear_objective_instance = LinearObjective([3, 4, 2, 2, 7], 'max')
        objective_function_instance.set_objective(linear_objective_instance)
        objective_function_instance.solve_dd()
        
        file_path = os.path.join('Test', 'test_prints', 'solutionDDIndependentSet.txt')
        
        with open(file_path, "r") as file:
            expected_output = file.read()

        actual_output = mock_stdout.getvalue()

        self.assertEqual(actual_output.strip(), expected_output.strip())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_solution_for_reduceDD(self, mock_stdout):
        dd_independent_set_instance = DD(self.independent_set_instance, verbose=False)
        dd_independent_set_instance.create_reduce_decision_diagram(verbose=False)

        objective_function_instance = ObjectiveFunction(dd_independent_set_instance)
        linear_objective_instance = LinearObjective([3, 4, 2, 2, 7], 'max')
        objective_function_instance.set_objective(linear_objective_instance)
        objective_function_instance.solve_dd()
        
        file_path = os.path.join('Test', 'test_prints', 'solutionReduceDDIndependentSet.txt')
        
        with open(file_path, "r") as file:
            expected_output = file.read()

        actual_output = mock_stdout.getvalue()

        self.assertEqual(actual_output.strip(), expected_output.strip())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_solution_for_restrictedDD(self, mock_stdout):
        dd_independent_set_instance = DD(self.independent_set_instance, verbose=False)
        dd_independent_set_instance.create_restricted_decision_diagram(verbose=False, max_width=2)

        objective_function_instance = ObjectiveFunction(dd_independent_set_instance)
        linear_objective_instance = LinearObjective([3, 4, 2, 2, 7], 'max')
        objective_function_instance.set_objective(linear_objective_instance)
        objective_function_instance.solve_dd()
        
        file_path = os.path.join('Test', 'test_prints', 'solutionRestrictedDDIndependentSet.txt')
        
        with open(file_path, "r") as file:
            expected_output = file.read()

        actual_output = mock_stdout.getvalue()

        self.assertEqual(actual_output.strip(), expected_output.strip())
    
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_solution_for_relaxedDD(self, mock_stdout):
        dd_independent_set_instance = DD(self.independent_set_instance, verbose=False)
        dd_independent_set_instance.create_relaxed_decision_diagram(verbose=False, max_width=2)

        objective_function_instance = ObjectiveFunction(dd_independent_set_instance)
        linear_objective_instance = LinearObjective([3, 4, 2, 2, 7], 'max')
        objective_function_instance.set_objective(linear_objective_instance)
        objective_function_instance.solve_dd()
        
        file_path = os.path.join('Test', 'test_prints', 'solutionRelaxedDDIndependentSet.txt')
        
        with open(file_path, "r") as file:
            expected_output = file.read()

        actual_output = mock_stdout.getvalue()

        self.assertEqual(actual_output.strip(), expected_output.strip())
    
if __name__ == '__main__':
    unittest.main()