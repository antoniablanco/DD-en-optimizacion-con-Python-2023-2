def custom_equals(state_one, state_two):
    return state_one == state_two

def custom_transition_function(previus_state, variable, value):
    lista_suma_variables = [3,3,4,6]
    new_state = int(previus_state[0])+lista_suma_variables[int(variable[2:])-1]*value
    return new_state

def custom_factibility_function(state):
    return int(sum(state.state_values)) <= 4

