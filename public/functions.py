def custom_equals(state_one, state_two):
    return state_one == state_two

def custom_transition_function():
    input_state = input("Ingrese el estado del nodo: ")
    return input_state

def custom_factibility_function(state):
    return int(sum(state.state_values)) <= 4

