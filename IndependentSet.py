from Class.Problem import Problem
from Class.MDD import MDD

initial_state = [1,2,3,4,5]
ordered_variables = ['x_1','x_2','x_3','x_4', 'x_5']
variable_nature = [0, 1]



problem_instance = Problem(initial_state, ordered_variables, variable_nature)

def custom_equals(state_one, state_two):
    return set(state_one) == set(state_two)

def custom_transition_function(previus_state, variable_id, variable_value):
    DictVecinos = {'x_1':[2,3],'x_2':[1,3,4],'x_3':[1,2,4],'x_4':[2,3,5], 'x_5':[4]}
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
    
    return new_state

def custom_factibility_function(newState, existedState, variable_id, variable_value):
    return (int(variable_value) == 1 and int(variable_id[2:]) in existedState) or (int(variable_value) == 0)


problem_instance.define_equals_function(custom_equals)
problem_instance.define_transition_function(custom_transition_function)
problem_instance.define_factibility_function(custom_factibility_function)

mdd_instance = MDD(problem_instance)

print(mdd_instance.get_decision_diagram())
print(mdd_instance.get_reduce_decision_diagram())
print(mdd_instance.print_decision_diagram())
print(mdd_instance.print_reduce_decision_diagram())   
