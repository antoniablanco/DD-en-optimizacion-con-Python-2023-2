import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)

import unittest
from unittest.mock import patch
from Class.Problems.AbstractProblemClass import AbstractProblem
from Class.DD import DD
from Class.ObjectiveFunction.ObjectiveFunction import ObjectiveFunction, LinearObjectiveDP
from contextlib import contextmanager
import dd_controlled_generators.DDKnapsack as DDKnapsack
import dd_controlled_generators.ReduceDDKnapsack as ReduceDDKnapsack
import dd_controlled_generators.RestrictedDDKnapsack as RestrictedDDKnapsack
import dd_controlled_generators.FalseDDKnapsack as FalseDDKnapsack
import dd_controlled_generators.RelaxedDDKnapsack as RelaxedDDKnapsack
import io
import os


@contextmanager
def assertNoRaise():
    try:
        yield
    except Exception as e:
        raise AssertionError(f"Se generó una excepción: {e}")


class ProblemKnapsackTest(unittest.TestCase):
    def setUp(self):
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
            
            def get_priority_for_discard_node(self, state):
                total = 0
                for i in range(len(state)):
                    total += state[i]
                return total
            
            def get_priority_for_merge_nodes(self, id_node, state):
                return -int(id_node)

            def merge_operator(self, state_one, state_two):
                state = []
                for i in range(len(state_one)):
                    state.append(max(state_one[i], state_two[i]))
                return state

        knpasack_initial_state = [0]
        knpasack_variables = [('x_1', [0, 1]), ('x_2', [0, 1]), ('x_3', [0, 1]), ('x_4', [0, 1])]
        self.knapsack_instance = ProblemKnapsack(knpasack_initial_state, knpasack_variables)
        self.dd_knapsack_instance = DD(self.knapsack_instance, verbose=True)

    def test_ordered_variables(self):
        ordered_variables_test = ['x_1', 'x_2', 'x_3', 'x_4']
        self.assertEqual(self.knapsack_instance.ordered_variables, ordered_variables_test)
    
    def test_variables_domain(self):
        variables_domain_test = {'x_1': [0, 1], 'x_2': [0, 1], 'x_3': [0, 1], 'x_4': [0, 1]}
        self.assertEqual(self.knapsack_instance.variables_domain, variables_domain_test)

    def test_is_dd_created(self):
        dd_knapsack_instance = DD(self.knapsack_instance, verbose=True)
        self.assertIsNotNone(dd_knapsack_instance.graph_DD)
    
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_verbose_create_dd(self, mock_stdout):
        dd_knapsack_instance = DD(self.knapsack_instance, verbose=True)

        file_path = os.path.join('Test', 'test_prints', 'createDDKnapsack.txt')
        
        with open(file_path, "r") as file:
            expected_output = file.read()

        actual_output = mock_stdout.getvalue()

        self.assertEqual(actual_output.strip(), expected_output.strip())
    
    def test_create_dd_graph_equal(self):
        resultado = self.dd_knapsack_instance.graph_DD == DDKnapsack.graph

        self.assertTrue(resultado)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_verbose_create_reduce_dd(self, mock_stdout):
        self.dd_knapsack_instance.create_reduce_decision_diagram(verbose=True)

        file_path = os.path.join('Test', 'test_prints', 'createReduceDDKnapsack.txt')
        
        with open(file_path, "r") as file:
            expected_output = file.read()

        actual_output = mock_stdout.getvalue()

        self.assertEqual(actual_output.strip(), expected_output.strip())

    def test_create_reduce_dd_graph_equal(self):
        self.dd_knapsack_instance.create_reduce_decision_diagram(verbose=False)
        resultado = self.dd_knapsack_instance.graph_DD == ReduceDDKnapsack.graph

        self.assertTrue(resultado)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_verbose_create_restricted_dd(self, mock_stdout):
        self.dd_knapsack_instance.create_restricted_decision_diagram(verbose=True, max_width=3)

        file_path = os.path.join('Test', 'test_prints', 'createRestrictedDDKnapsack.txt')
        
        with open(file_path, "r") as file:
            expected_output = file.read()

        actual_output = mock_stdout.getvalue()

        self.assertEqual(actual_output.strip(), expected_output.strip())
    
    def test_create_restricted_dd_graph_equal(self):
        self.dd_knapsack_instance.create_restricted_decision_diagram(verbose=False, max_width=3)
        resultado = self.dd_knapsack_instance.graph_DD == RestrictedDDKnapsack.graph

        self.assertTrue(resultado)
    
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_verbose_create_relaxed_dd(self, mock_stdout):
        self.dd_knapsack_instance.create_relaxed_decision_diagram(verbose=True, max_width=3)

        file_path = os.path.join('Test', 'test_prints', 'createRelaxedDDKnapsack.txt')
        
        with open(file_path, "r") as file:
            expected_output = file.read()

        actual_output = mock_stdout.getvalue()

        self.assertEqual(actual_output.strip(), expected_output.strip())
    
    def test_create_relaxed_dd_graph_equal(self):
        self.dd_knapsack_instance.create_relaxed_decision_diagram(verbose=False, max_width=3)
        resultado = self.dd_knapsack_instance.graph_DD == RelaxedDDKnapsack.graph

        self.assertTrue(resultado)

    def test_get_dd_graph(self):
        self.assertIsNotNone(self.dd_knapsack_instance.get_decision_diagram_graph())
    
    @patch('matplotlib.pyplot.show')
    def test_print_dd_graph(self, mock_show):
        with assertNoRaise():
            self.dd_knapsack_instance.print_decision_diagram()
            mock_show.assert_called_once()

    def test_get_copy(self):
        self.assertIsNot(self.dd_knapsack_instance.graph_DD, self.dd_knapsack_instance.get_decision_diagram_graph_copy)

    def test_get_DDBuilder_time(self):
        self.assertTrue(self.dd_knapsack_instance.dd_builder_time > 0)
    
    def test_get_ReduceDDBuilder_time(self):
        self.dd_knapsack_instance.create_reduce_decision_diagram(verbose=False)
        self.assertTrue(self.dd_knapsack_instance.reduce_dd_builder_time > 0)
    
    def test_get_RestrictedDDBuilder_time(self):
        self.dd_knapsack_instance.create_restricted_decision_diagram(verbose=False, max_width=3)
        self.assertTrue(self.dd_knapsack_instance.restricted_dd_builder_time > 0)
    
    def test_get_RelaxedDDBuilder_time(self):
        self.dd_knapsack_instance.create_relaxed_decision_diagram(verbose=False, max_width=3)
        self.assertTrue(self.dd_knapsack_instance.relaxed_dd_builder_time > 0)
    
    def test_get_solution_for_DD(self):

        value, path = self.get_value_path_solution()
        
        expected_value = 18
        expected_path = ' arc_0_1(0)-> arc_1_3(0)-> arc_3_7(1)-> arc_7_10(0)'

        self.assertEqual(value, expected_value)
        self.assertEqual(path, expected_path)

    def test_get_solution_for_reduceDD(self):
        self.dd_knapsack_instance.create_reduce_decision_diagram(verbose=False)

        value, path = self.get_value_path_solution()
        
        expected_value = 18
        expected_path = ' arc_0_1(0)-> arc_1_3(0)-> arc_3_6(1)-> arc_6_7(0)'

        self.assertEqual(value, expected_value)
        self.assertEqual(path, expected_path)

    def test_get_solution_for_restrictedDD(self):
        self.dd_knapsack_instance.create_restricted_decision_diagram(verbose=False, max_width=3)
        
        value, path = self.get_value_path_solution()
        
        expected_value = 18
        expected_path = ' arc_0_1(0)-> arc_1_3(0)-> arc_3_6(1)-> arc_6_8(0)'

        self.assertEqual(value, expected_value)
        self.assertEqual(path, expected_path)
    
    def test_get_solution_for_relaxedDD(self):
        self.dd_knapsack_instance.create_relaxed_decision_diagram(verbose=False, max_width=3)

        value, path = self.get_value_path_solution()
        
        expected_value = 18
        expected_path = ' arc_0_1(0)-> arc_1_3(0)-> arc_3_6(1)-> arc_6_9(0)'

        self.assertEqual(value, expected_value)
        self.assertEqual(path, expected_path)
    
    def test_compare_two_diferent_graphs(self):
        self.dd_knapsack_instance.create_reduce_decision_diagram(verbose=False)

        self.assertFalse(self.dd_knapsack_instance.graph_DD == FalseDDKnapsack.graph)
    
    def test_compare_gml_dd_graph(self):
        self.dd_knapsack_instance.export_graph_file('test')

        expected_file_path = os.path.join('Test', 'gml_files', 'exact_dd_knapsack.gml')
        actual_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'test.gml'))

        self.assertTrue(os.path.exists(actual_file_path))
        self.assertTrue(os.path.exists(expected_file_path))

        with open(expected_file_path, "r") as file:
            expected_output = file.read()
        
        with open(actual_file_path, "r") as file:
            actual_output = file.read()
        
        self.assertEqual(actual_output.strip(), expected_output.strip())
    
    def test_compare_gml_reduce_dd_graph(self):
        self.dd_knapsack_instance.create_reduce_decision_diagram(verbose=False)
        self.dd_knapsack_instance.export_graph_file('test')

        expected_file_path = os.path.join('Test', 'gml_files', 'reduce_dd_knapsack.gml')
        actual_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'test.gml'))

        self.assertTrue(os.path.exists(actual_file_path))
        self.assertTrue(os.path.exists(expected_file_path))

        with open(expected_file_path, "r") as file:
            expected_output = file.read()
        
        with open(actual_file_path, "r") as file:
            actual_output = file.read()
        
        self.assertEqual(actual_output.strip(), expected_output.strip())
    
    def test_compare_gml_restricted_dd_graph(self):
        self.dd_knapsack_instance.create_restricted_decision_diagram(verbose=False, max_width=3)
        self.dd_knapsack_instance.export_graph_file('test')

        expected_file_path = os.path.join('Test', 'gml_files', 'restricted_dd_knapsack.gml')
        actual_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'test.gml'))

        self.assertTrue(os.path.exists(actual_file_path))
        self.assertTrue(os.path.exists(expected_file_path))

        with open(expected_file_path, "r") as file:
            expected_output = file.read()
        
        with open(actual_file_path, "r") as file:
            actual_output = file.read()
        
        self.assertEqual(actual_output.strip(), expected_output.strip())
    
    def test_compare_gml_relax_dd_graph(self):
        self.dd_knapsack_instance.create_relaxed_decision_diagram(verbose=False, max_width=3)
        self.dd_knapsack_instance.export_graph_file('test')

        expected_file_path = os.path.join('Test', 'gml_files', 'relax_dd_knapsack.gml')
        actual_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'test.gml'))

        self.assertTrue(os.path.exists(actual_file_path))
        self.assertTrue(os.path.exists(expected_file_path))

        with open(expected_file_path, "r") as file:
            expected_output = file.read()
        
        with open(actual_file_path, "r") as file:
            actual_output = file.read()
        
        self.assertEqual(actual_output.strip(), expected_output.strip())

    def get_value_path_solution(self):
        objective_function_instance = ObjectiveFunction(self.dd_knapsack_instance)
        linear_objective_instance = LinearObjectiveDP([-5, 1, 18, 17], 'max')
        objective_function_instance.set_objective(linear_objective_instance)
        answer = objective_function_instance.solve_dd()
        return answer[0], answer[1]

if __name__ == '__main__':
    unittest.main()