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
                return -total
            
            def get_priority_for_merge_nodes(self, id_node):
                return -int(id_node)

            def merge_operator(self, state_one, state_two):
                state = []
                for i in range(len(state_one)):
                    state.append(max(state_one[i], state_two[i]))
                return state

        knpasack_initial_state = [0]
        knpasack_variables = [('x_1', [0, 1]), ('x_2', [0, 1]), ('x_3', [0, 1]), ('x_4', [0, 1])]
        self.knapsack_instance = ProblemKnapsack(knpasack_initial_state, knpasack_variables)

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
        dd_knapsack_instance = DD(self.knapsack_instance, verbose=False)
        resultado = dd_knapsack_instance.graph_DD == DDKnapsack.graph

        self.assertTrue(resultado)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_verbose_create_reduce_dd(self, mock_stdout):
        dd_knapsack_instance = DD(self.knapsack_instance, verbose=False)
        dd_knapsack_instance.create_reduce_decision_diagram(verbose=True)

        file_path = os.path.join('Test', 'test_prints', 'createReduceDDKnapsack.txt')
        
        with open(file_path, "r") as file:
            expected_output = file.read()

        actual_output = mock_stdout.getvalue()

        self.assertEqual(actual_output.strip(), expected_output.strip())

    def test_create_reduce_dd_graph_equal(self):
        dd_knapsack_instance = DD(self.knapsack_instance, verbose=False)
        dd_knapsack_instance.create_reduce_decision_diagram(verbose=False)
        resultado = dd_knapsack_instance.graph_DD == ReduceDDKnapsack.graph

        self.assertTrue(resultado)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_verbose_create_restricted_dd(self, mock_stdout):
        dd_knapsack_instance = DD(self.knapsack_instance, verbose=False)
        dd_knapsack_instance.create_restricted_decision_diagram(verbose=True, max_width=3)

        file_path = os.path.join('Test', 'test_prints', 'createRestrictedDDKnapsack.txt')
        
        with open(file_path, "r") as file:
            expected_output = file.read()

        actual_output = mock_stdout.getvalue()

        self.assertEqual(actual_output.strip(), expected_output.strip())
    
    def test_create_restricted_dd_graph_equal(self):
        dd_knapsack_instance = DD(self.knapsack_instance, verbose=False)
        dd_knapsack_instance.create_restricted_decision_diagram(verbose=False, max_width=3)
        resultado = dd_knapsack_instance.graph_DD == RestrictedDDKnapsack.graph

        self.assertTrue(resultado)
    
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_verbose_create_relaxed_dd(self, mock_stdout):
        dd_knapsack_instance = DD(self.knapsack_instance, verbose=False)
        dd_knapsack_instance.create_relaxed_decision_diagram(verbose=True, max_width=3)

        file_path = os.path.join('Test', 'test_prints', 'createRelaxedDDKnapsack.txt')
        
        with open(file_path, "r") as file:
            expected_output = file.read()

        actual_output = mock_stdout.getvalue()

        self.assertEqual(actual_output.strip(), expected_output.strip())
    
    def test_create_relaxed_dd_graph_equal(self):
        dd_knapsack_instance = DD(self.knapsack_instance, verbose=False)
        dd_knapsack_instance.create_relaxed_decision_diagram(verbose=False, max_width=3)
        resultado = dd_knapsack_instance.graph_DD == RelaxedDDKnapsack.graph

        self.assertTrue(resultado)

    def test_get_dd_graph(self):
        dd_knapsack_instance = DD(self.knapsack_instance, verbose=False)
        self.assertIsNotNone(dd_knapsack_instance.get_decision_diagram_graph())
    
    @patch('matplotlib.pyplot.show')
    def test_print_dd_graph(self, mock_show):
        dd_knapsack_instance = DD(self.knapsack_instance, verbose=False)

        with assertNoRaise():
            dd_knapsack_instance.print_decision_diagram()
            mock_show.assert_called_once()

    def test_get_copy(self):
        dd_knapsack_instance = DD(self.knapsack_instance, verbose=False)
        self.assertIsNot(dd_knapsack_instance.graph_DD, dd_knapsack_instance.get_decision_diagram_graph_copy)

    def test_get_DDBuilder_time(self):
        dd_knapsack_instance = DD(self.knapsack_instance, verbose=False)
        self.assertTrue(dd_knapsack_instance.dd_builder_time > 0)
    
    def test_get_ReduceDDBuilder_time(self):
        dd_knapsack_instance = DD(self.knapsack_instance, verbose=False)
        dd_knapsack_instance.create_reduce_decision_diagram(verbose=False)
        self.assertTrue(dd_knapsack_instance.reduce_dd_builder_time > 0)
    
    def test_get_RestrictedDDBuilder_time(self):
        dd_knapsack_instance = DD(self.knapsack_instance, verbose=False)
        dd_knapsack_instance.create_restricted_decision_diagram(verbose=False, max_width=3)
        self.assertTrue(dd_knapsack_instance.restricted_dd_builder_time > 0)
    
    def test_get_RelaxedDDBuilder_time(self):
        dd_knapsack_instance = DD(self.knapsack_instance, verbose=False)
        dd_knapsack_instance.create_relaxed_decision_diagram(verbose=False, max_width=3)
        self.assertTrue(dd_knapsack_instance.relaxed_dd_builder_time > 0)
    
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_solution_for_DD(self, mock_stdout):
        dd_knapsack_instance = DD(self.knapsack_instance, verbose=False)

        objective_function_instance = ObjectiveFunction(dd_knapsack_instance)
        linear_objective_instance = LinearObjective([-5, 1, 18, 17], 'max')
        objective_function_instance.set_objective(linear_objective_instance)
        objective_function_instance.solve_dd()
        
        file_path = os.path.join('Test', 'test_prints', 'solutionDDKnapsack.txt')
        
        with open(file_path, "r") as file:
            expected_output = file.read()

        actual_output = mock_stdout.getvalue()

        self.assertEqual(actual_output.strip(), expected_output.strip())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_solution_for_reduceDD(self, mock_stdout):
        dd_knapsack_instance = DD(self.knapsack_instance, verbose=False)
        dd_knapsack_instance.create_reduce_decision_diagram(verbose=False)

        objective_function_instance = ObjectiveFunction(dd_knapsack_instance)
        linear_objective_instance = LinearObjective([-5, 1, 18, 17], 'max')
        objective_function_instance.set_objective(linear_objective_instance)
        objective_function_instance.solve_dd()
        
        file_path = os.path.join('Test', 'test_prints', 'solutionReduceDDKnapsack.txt')
        
        with open(file_path, "r") as file:
            expected_output = file.read()

        actual_output = mock_stdout.getvalue()

        self.assertEqual(actual_output.strip(), expected_output.strip())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_solution_for_restrictedDD(self, mock_stdout):
        dd_knapsack_instance = DD(self.knapsack_instance, verbose=False)
        dd_knapsack_instance.create_restricted_decision_diagram(verbose=False, max_width=3)

        objective_function_instance = ObjectiveFunction(dd_knapsack_instance)
        linear_objective_instance = LinearObjective([-5, 1, 18, 17], 'max')
        objective_function_instance.set_objective(linear_objective_instance)
        objective_function_instance.solve_dd()
        
        file_path = os.path.join('Test', 'test_prints', 'solutionRestrictedDDKnapsack.txt')
        
        with open(file_path, "r") as file:
            expected_output = file.read()

        actual_output = mock_stdout.getvalue()

        self.assertEqual(actual_output.strip(), expected_output.strip())
    
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_solution_for_relaxedDD(self, mock_stdout):
        dd_knapsack_instance = DD(self.knapsack_instance, verbose=False)
        dd_knapsack_instance.create_relaxed_decision_diagram(verbose=False, max_width=3)

        objective_function_instance = ObjectiveFunction(dd_knapsack_instance)
        linear_objective_instance = LinearObjective([-5, 1, 18, 17], 'max')
        objective_function_instance.set_objective(linear_objective_instance)
        objective_function_instance.solve_dd()
        
        file_path = os.path.join('Test', 'test_prints', 'solutionRelaxedDDKnapsack.txt')
        
        with open(file_path, "r") as file:
            expected_output = file.read()

        actual_output = mock_stdout.getvalue()

        self.assertEqual(actual_output.strip(), expected_output.strip())
    
    def test_compare_two_diferent_graphs(self):
        dd_knapsack_instance = DD(self.knapsack_instance, verbose=False)
        dd_knapsack_instance.create_reduce_decision_diagram(verbose=False)

        self.assertFalse(dd_knapsack_instance.graph_DD == FalseDDKnapsack.graph)

if __name__ == '__main__':
    unittest.main()