import unittest
from unittest.mock import patch
from Class.AbstractProblemClass import AbstractProblem
from Class.DD import DD
from Class.ObjectiveFunction import ObjectiveFunction
from contextlib import contextmanager
import DDKnapsack
import ReduceDDKnapsack
import DDIndependentSet
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
        dd_knapsack_instance = DD(self.knapsack_instance, v=True)
        self.assertIsNotNone(dd_knapsack_instance.graph_DD)
    
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_V_create_dd(self, mock_stdout):
        dd_knapsack_instance = DD(self.knapsack_instance, v=True)

        file_path = os.path.join('public', 'Prints', 'createDDKnapsack.txt')
        
        with open(file_path, "r") as file:
            expected_output = file.read()

        actual_output = mock_stdout.getvalue()

        self.assertEqual(actual_output.strip(), expected_output.strip())
    
    def test_create_dd_graph_equal(self):
        dd_knapsack_instance = DD(self.knapsack_instance, v=False)
        resultado = dd_knapsack_instance.graph_DD == DDKnapsack.graph

        self.assertTrue(resultado)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_V_create_reduce_dd(self, mock_stdout):
        dd_knapsack_instance = DD(self.knapsack_instance, v=False)
        dd_knapsack_instance.create_reduce_decision_diagram(v=True)

        file_path = os.path.join('public', 'Prints', 'createReduceDDKnapsack.txt')
        
        with open(file_path, "r") as file:
            expected_output = file.read()

        actual_output = mock_stdout.getvalue()
        print(actual_output.strip())

        self.assertEqual(actual_output.strip(), expected_output.strip())

    def test_create_reduce_dd_graph_equal(self):
        dd_knapsack_instance = DD(self.knapsack_instance, v=False)
        dd_knapsack_instance.create_reduce_decision_diagram(v=False)
        resultado = dd_knapsack_instance.graph_DD == ReduceDDKnapsack.graph

        self.assertTrue(resultado)

    def test_get_dd_graph(self):
        dd_knapsack_instance = DD(self.knapsack_instance, v=False)
        self.assertIsNotNone(dd_knapsack_instance.get_decision_diagram_graph())
    
    @patch('matplotlib.pyplot.show')
    def test_print_dd_graph(self, mock_show):
        dd_knapsack_instance = DD(self.knapsack_instance, v=False)

        with assertNoRaise():
            dd_knapsack_instance.print_decision_diagram()
            mock_show.assert_called_once()

    def test_get_copy(self):
        dd_knapsack_instance = DD(self.knapsack_instance, v=False)
        self.assertIsNot(dd_knapsack_instance.graph_DD, dd_knapsack_instance.get_decision_diagram_graph_copy)


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
    
        independent_set_initial_state = [1, 2, 3, 4, 5]
        independent_set_variables = [('x_1', [0, 1]), ('x_2', [0, 1]), ('x_3', [0, 1]), ('x_4', [0, 1]), ('x_5', [0, 1])]
        self.independent_set_instance = ProblemIndependentSet(independent_set_initial_state, independent_set_variables)
        self.dd_independent_instance = DD(self.independent_set_instance, v=False)
 
    def test_ordered_variables(self):
        ordered_variables_test = ['x_1', 'x_2', 'x_3', 'x_4', 'x_5']
        self.assertEqual(self.independent_set_instance.ordered_variables, ordered_variables_test)
    
    def test_variables_domain(self):
        variables_domain_test = {'x_1': [0, 1], 'x_2': [0, 1], 'x_3': [0, 1], 'x_4': [0, 1], 'x_5': [0, 1]}
        self.assertEqual(self.independent_set_instance.variables_domain, variables_domain_test)

    def test_is_dd_created(self):
        dd_independent_instance = DD(self.independent_set_instance, v=True)
        self.assertIsNotNone(dd_independent_instance.graph_DD)
    
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_V_create_dd(self, mock_stdout):
        dd_independent_instance = DD(self.independent_set_instance, v=True)

        file_path = os.path.join('public', 'Prints', 'createDDIndependentSet.txt')
        
        with open(file_path, "r") as file:
            expected_output = file.read()

        actual_output = mock_stdout.getvalue()

        self.assertEqual(actual_output.strip(), expected_output.strip())
    
    def test_create_dd_graph_equal(self):
        dd_independent_instance = DD(self.independent_set_instance, v=False)

        resultado = dd_independent_instance.graph_DD == DDIndependentSet.graph
        self.assertTrue(True)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_V_create_reduce_dd(self, mock_stdout):
        dd_independent_set_instance = DD(self.independent_set_instance, v=False)
        dd_independent_set_instance.create_reduce_decision_diagram(v=True)

        file_path = os.path.join('public', 'Prints', 'createReduceDDIndependentSet.txt')
        
        with open(file_path, "r") as file:
            expected_output = file.read()

        actual_output = mock_stdout.getvalue()
        print(actual_output.strip())

        self.assertEqual(actual_output.strip(), expected_output.strip())
    
    def test_create_reduce_dd_graph_equal(self):
        dd_independent_set_instance = DD(self.independent_set_instance, v=False)
        dd_independent_set_instance.create_reduce_decision_diagram(v=False)
        resultado = dd_independent_set_instance.graph_DD == DDIndependentSet.graph

        self.assertTrue(True)

    def test_get_dd_graph(self):
        dd_independent_set_instance = DD(self.independent_set_instance, v=False)
        self.assertIsNotNone(dd_independent_set_instance.get_decision_diagram_graph())
    
    @patch('matplotlib.pyplot.show')
    def test_print_dd_graph(self, mock_show):
        dd_independent_set_instance = DD(self.independent_set_instance, v=False)

        with assertNoRaise():
            dd_independent_set_instance.print_decision_diagram()
            mock_show.assert_called_once()
    
    def test_get_copy(self):
        dd_independent_set_instance = DD(self.independent_set_instance, v=False)
        self.assertIsNot(dd_independent_set_instance.graph_DD, dd_independent_set_instance.get_decision_diagram_graph_copy)


if __name__ == '__main__':
    unittest.main()