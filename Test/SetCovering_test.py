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
from Class.ObjectiveFunction.ObjectiveFunction import ObjectiveFunction, LinearObjectiveDP
from contextlib import contextmanager
import dd_controlled_generators.DDSetCovering as DDSetCovering
import dd_controlled_generators.RestrictedDDSetCovering as RestrictedDDSetCovering
import dd_controlled_generators.RelaxedDDSetCovering as RelaxedDDSetCovering

@contextmanager
def assertNoRaise():
    try:
        yield
    except Exception as e:
        raise AssertionError(f"Se generó una excepción: {e}")


class SetCoveringTest(unittest.TestCase):
    def setUp(self):
        class SetCoveringProblem(AbstractProblem):

            def __init__(self, initial_state, variables, matrix_of_wheight, right_side_of_restrictions):
                super().__init__(initial_state, variables)

                self.matrix_of_wheight = matrix_of_wheight
                self.right_side_of_restrictions = right_side_of_restrictions

            def equals(self, state_one, state_two):
                return set(state_one) == set(state_two)

            def transition_function(self, previus_state, variable_id, variable_value):
                isFeasible = True

                if int(variable_value) == 0:
                    new_state = previus_state.copy()
                    for row in previus_state:
                        maximo = len(self.matrix_of_wheight[row-1]) - self.matrix_of_wheight[row-1][::-1].index(1) 
                        if int(variable_id[2:]) >= maximo:
                            isFeasible = False 
                else:
                    new_state = []
                    for row in previus_state:
                        if self.matrix_of_wheight[row-1][int(variable_id[2:])-1] != 1:
                            new_state.append(row)
                
                return new_state, isFeasible
            
            def get_priority_for_discard_node(self, state):
                return len(state)
            
            def get_priority_for_merge_nodes(self, id_node, state):
                return len(state)

            def merge_operator(self, state_one, state_two):
                return list(set(state_one) & set(state_two))
    
        initial_state = [1, 2, 3]
        variables = [('x_1', [0, 1]), ('x_2', [0, 1]), ('x_3', [0, 1]), ('x_4', [0, 1]), ('x_5', [0, 1]), ('x_6', [0, 1])]

        matrix_of_wheight = [[1, 1, 1, 0, 0, 0],
                     [1, 0, 0, 1, 1, 0],
                     [0, 1, 0, 1, 0, 1]]

        right_side_of_restrictions = [1, 1, 1]
        self.problem_instance = SetCoveringProblem(initial_state, variables, matrix_of_wheight, right_side_of_restrictions)
        self.dd_instance = DD(self.problem_instance, verbose=False)
 
    def test_ordered_variables(self):
        ordered_variables_test = ['x_1', 'x_2', 'x_3', 'x_4', 'x_5', 'x_6']
        self.assertEqual(self.problem_instance.ordered_variables, ordered_variables_test)
    
    def test_variables_domain(self):
        variables_domain_test = {'x_1': [0, 1], 'x_2': [0, 1], 'x_3': [0, 1], 'x_4': [0, 1], 'x_5': [0, 1], 'x_6': [0, 1]}
        self.assertEqual(self.problem_instance.variables_domain, variables_domain_test)

    def test_is_dd_created(self):
        self.assertIsNotNone(self.dd_instance.graph_DD)
    
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_verbose_create_dd(self, mock_stdout):
        dd_independent_instance = DD(self.problem_instance, verbose=True)

        file_path = os.path.join('Test', 'test_prints', 'createDDSetCovering.txt')
        
        with open(file_path, "r") as file:
            expected_output = file.read()

        actual_output = mock_stdout.getvalue()

        self.assertEqual(actual_output.strip(), expected_output.strip())
    
    def test_create_dd_graph_equal(self):
        resultado = self.dd_instance.graph_DD == DDSetCovering.graph
        self.assertTrue(resultado)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_verbose_create_reduce_dd(self, mock_stdout):
        self.dd_instance.create_reduce_decision_diagram(verbose=True)

        file_path = os.path.join('Test', 'test_prints', 'createReduceDDSetCovering.txt')
        
        with open(file_path, "r") as file:
            expected_output = file.read()

        actual_output = mock_stdout.getvalue()

        self.assertEqual(actual_output.strip(), expected_output.strip())
    
    def test_create_reduce_dd_graph_equal(self):
        self.dd_instance.create_reduce_decision_diagram(verbose=False)
        resultado = (self.dd_instance.graph_DD == DDSetCovering.graph)
        self.assertTrue(resultado)
    
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_verbose_create_restricted_dd(self, mock_stdout):
        self.dd_instance.create_restricted_decision_diagram(verbose=True, max_width=3)

        file_path = os.path.join('Test', 'test_prints', 'createRestrictedDDSetCovering.txt')
        
        with open(file_path, "r") as file:
            expected_output = file.read()

        actual_output = mock_stdout.getvalue()

        self.assertEqual(actual_output.strip(), expected_output.strip())

    def test_create_restricted_dd_graph_equal(self):
        self.dd_instance.create_restricted_decision_diagram(verbose=False, max_width=3)
        resultado = self.dd_instance.graph_DD == RestrictedDDSetCovering.graph

        self.assertTrue(resultado)
    
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_verbose_create_relaxed_dd(self, mock_stdout):
        self.dd_instance.create_relaxed_decision_diagram(verbose=True, max_width=3)

        file_path = os.path.join('Test', 'test_prints', 'createRelaxedDDSetCovering.txt')
        
        with open(file_path, "r") as file:
            expected_output = file.read()

        actual_output = mock_stdout.getvalue()

        self.assertEqual(actual_output.strip(), expected_output.strip())

    def test_create_relaxed_dd_graph_equal(self):
        self.dd_instance.create_relaxed_decision_diagram(verbose=False, max_width=3)
        resultado = self.dd_instance.graph_DD == RelaxedDDSetCovering.graph

        self.assertTrue(resultado)
    
    def test_get_dd_graph(self):
        self.assertIsNotNone(self.dd_instance.get_decision_diagram_graph())
    
    @patch('matplotlib.pyplot.show')
    def test_print_dd_graph(self, mock_show):

        with assertNoRaise():
            self.dd_instance.print_decision_diagram()
            mock_show.assert_called_once()
    
    def test_get_copy(self):
        self.assertIsNot(self.dd_instance.graph_DD, self.dd_instance.get_decision_diagram_graph_copy)

    def test_get_DDBuilder_time(self):
        self.assertTrue(self.dd_instance.dd_builder_time > 0)
    
    def test_get_ReduceDDBuilder_time(self):
        self.dd_instance.create_reduce_decision_diagram(verbose=False)
        self.assertTrue(self.dd_instance.reduce_dd_builder_time > 0)
    
    def test_get_RestrictedDDBuilder_time(self):
        self.dd_instance.create_restricted_decision_diagram(verbose=False, max_width=2)
        self.assertTrue(self.dd_instance.restricted_dd_builder_time > 0)
    
    def test_get_RelaxedDDBuilder_time(self):
        self.dd_instance.create_relaxed_decision_diagram(verbose=False, max_width=2)
        self.assertTrue(self.dd_instance.relaxed_dd_builder_time > 0)
    
    def test_get_solution_for_DD(self): 

        value, path = self.get_value_path_solution()
        print("value: ", value)
        print("path: ", path)
        expected_value = 3
        expected_path = ' arc_0_2(1)-> arc_2_6(1)-> arc_6_10(0)-> arc_10_12(0)-> arc_12_16(0)-> arc_16_17(0)'

        self.assertEqual(value, expected_value)
        self.assertEqual(path, expected_path)

    def test_get_solution_for_reduceDD(self):
        self.dd_instance.create_reduce_decision_diagram(verbose=False)

        value, path = self.get_value_path_solution()
        
        expected_value = 3
        expected_path = ' arc_0_2(1)-> arc_2_6(1)-> arc_6_10(0)-> arc_10_12(0)-> arc_12_16(0)-> arc_16_17(0)'

        self.assertEqual(value, expected_value)
        self.assertEqual(path, expected_path)

    def test_get_solution_for_restrictedDD(self):
        self.dd_instance.create_restricted_decision_diagram(verbose=False, max_width=3)

        value, path = self.get_value_path_solution()
        
        expected_value = 3
        expected_path = ' arc_0_2(1)-> arc_2_5(1)-> arc_5_8(0)-> arc_8_10(0)-> arc_10_12(0)-> arc_12_14(0)'

        self.assertEqual(value, expected_value)
        self.assertEqual(path, expected_path)
    
    def test_get_solution_for_relaxedDD(self):
        self.dd_instance.create_relaxed_decision_diagram(verbose=False, max_width=3)

        value, path = self.get_value_path_solution()
        
        expected_value = 3
        expected_path = ' arc_0_1(0)-> arc_1_3(0)-> arc_3_6(0)-> arc_6_10(1)-> arc_10_12(0)-> arc_12_14(0)'

        self.assertEqual(value, expected_value)
        self.assertEqual(path, expected_path)
    
    def test_compare_gml_exact_dd_graph(self):
        self.dd_instance.export_graph_file('test')

        expected_file_path = os.path.join('Test', 'gml_files', 'exact_dd_set_covering.gml')
        actual_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'test.gml'))

        self.assertTrue(os.path.exists(actual_file_path))
        self.assertTrue(os.path.exists(expected_file_path))

        with open(expected_file_path, "r") as file:
            expected_output = file.read()
        
        with open(actual_file_path, "r") as file:
            actual_output = file.read()
        
        self.assertEqual(actual_output.strip(), expected_output.strip())
    
    def test_compare_gml_reduce_dd_graph(self):
        self.dd_instance.create_reduce_decision_diagram(verbose=False)
        self.dd_instance.export_graph_file('test')

        expected_file_path = os.path.join('Test', 'gml_files', 'reduce_dd_set_covering.gml')
        actual_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'test.gml'))

        self.assertTrue(os.path.exists(actual_file_path))
        self.assertTrue(os.path.exists(expected_file_path))

        with open(expected_file_path, "r") as file:
            expected_output = file.read()
        
        with open(actual_file_path, "r") as file:
            actual_output = file.read()
        
        self.assertEqual(actual_output.strip(), expected_output.strip())
    
    def test_compare_gml_restricted_dd_graph(self):
        self.dd_instance.create_restricted_decision_diagram(verbose=False, max_width=3)
        self.dd_instance.export_graph_file('test')

        expected_file_path = os.path.join('Test', 'gml_files', 'restricted_dd_set_covering.gml')
        actual_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'test.gml'))

        self.assertTrue(os.path.exists(actual_file_path))
        self.assertTrue(os.path.exists(expected_file_path))

        with open(expected_file_path, "r") as file:
            expected_output = file.read()
        
        with open(actual_file_path, "r") as file:
            actual_output = file.read()
        
        self.assertEqual(actual_output.strip(), expected_output.strip())
    
    def test_compare_gml_relax_dd_graph(self):
        self.dd_instance.create_relaxed_decision_diagram(verbose=False, max_width=3)
        self.dd_instance.export_graph_file('test')

        expected_file_path = os.path.join('Test', 'gml_files', 'relax_dd_set_covering.gml')
        actual_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'test.gml'))

        self.assertTrue(os.path.exists(actual_file_path))
        self.assertTrue(os.path.exists(expected_file_path))

        with open(expected_file_path, "r") as file:
            expected_output = file.read()
        
        with open(actual_file_path, "r") as file:
            actual_output = file.read()
        
        self.assertEqual(actual_output.strip(), expected_output.strip())
    
    def get_value_path_solution(self):
        objective_function_instance = ObjectiveFunction(self.dd_instance)
        linear_objective_instance = LinearObjectiveDP([2, 1, 4, 3, 4, 3], 'min')
        objective_function_instance.set_objective(linear_objective_instance)
        answer = objective_function_instance.solve_dd()
        return answer[0], answer[1]
if __name__ == '__main__':
    unittest.main()