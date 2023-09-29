from Class.Problem import Problem
from Class.MDD import MDD

initial_state = [0]
ordered_variables = ['x_1','x_2','x_3','x_4']
variable_nature = [0, 1]

problem_instance = Problem(initial_state, ordered_variables, variable_nature)

def custom_equals(state_one, state_two):
    return state_one == state_two

def custom_transition_function(previus_state, variable, value):
    lista_suma_variables = [3,3,4,6]
    new_state = int(previus_state[0])+lista_suma_variables[int(variable[2:])-1]*value
    return [new_state]

def custom_factibility_function(newState, existedState, variable_id, variable_value):
    return int(newState[0]) <= 5


problem_instance.define_equals_function(custom_equals)
problem_instance.define_transition_function(custom_transition_function)
problem_instance.define_factibility_function(custom_factibility_function)

mdd_instance = MDD(problem_instance)

print(mdd_instance.get_decision_diagram())
print(mdd_instance.get_reduce_decision_diagram())
print(mdd_instance.print_decision_diagram())
print(mdd_instance.print_reduce_decision_diagram())   
