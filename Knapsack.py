from Class.AbstractProblemClass import AbstractProblem
from Class.DD import DD
from Class.ObjectiveFunction import ObjectiveFunction
from Exceptions.MyExceptions import SameLenError

class ProblemKnapsack(AbstractProblem):

    def __init__(self, initial_state, variables, list_of_wheight_for_restrictions, right_side_of_restrictions):
        super().__init__(initial_state, variables)

        self.list_of_wheight_for_restrictions = list_of_wheight_for_restrictions
        self.right_side_of_restrictions = right_side_of_restrictions

        self.check_atributes(variables)

    def check_atributes(self, variables):
        self.check_same_len_matrix_and_right_side()
        self.check_same_len_rows_matrix_and_variables(variables)
    
    def check_same_len_matrix_and_right_side(self):
        if ((len(self.list_of_wheight_for_restrictions) != len(self.right_side_of_restrictions)) or (len(initial_state) != len(self.right_side_of_restrictions))):
            raise SameLenError("matrix_of_wheight and right_side_of_restrictions must have the same length")
    
    def check_same_len_rows_matrix_and_variables(self, variables):
        for row in range(len(self.list_of_wheight_for_restrictions)):
            if len(self.list_of_wheight_for_restrictions[row]) != len(variables):
                raise SameLenError("rows of matrix_of_wheight and right_side_of_restrictions must have the same length of variables")

    def equals(self, state_one, state_two):
        return set(state_one) == set(state_two)

    def transition_function(self, previus_state, variable_id, variable_value):
        isFeasible = True
        state = []
        for row in range(len(self.list_of_wheight_for_restrictions)):
            lista_suma_variables = self.list_of_wheight_for_restrictions[row]
            new_state = int(previus_state[row])+lista_suma_variables[int(variable_id[2:])-1]*int(variable_value)
            state.append(new_state)

            isFeasible_this_row = int(state[row]) <= self.right_side_of_restrictions[row]
            isFeasible = isFeasible and isFeasible_this_row
        return state, isFeasible

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

dd_instance = DD(problem_instance, v=False)

# Construcción del diagrama de decisión
dd_instance.print_decision_diagram()
dd_instance.create_reduce_decision_diagram(v=False)
dd_instance.print_decision_diagram()
dd_instance.export_graph_file("test")

decision_diagram = dd_instance.get_decision_diagram_graph()


# Resolución del diagrama
objective_function_instance = ObjectiveFunction(decision_diagram)
objective_function_instance.develop_solver([-5, 1, 18, 17], 'max')
objective_function_instance.solve_dd()

