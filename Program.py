from Class.Problem import Problem
from Class.MDD import MDD

initialState = [0]
orderedVariables = ['x_1','x_2','x_3','x_4']
variableNature = [0, 1]

problem_instance = Problem(initialState, orderedVariables, variableNature)

def CustomEquals(stateOne, stateTwo):
    return stateOne == stateTwo

def CustomTransitionFunction():
    input_state = input("Ingrese el estado del nodo: ")
    return input_state

def CustomFactibilityFunction(state):
    return int(state[0]) <= 6


problem_instance.DefineEqualsFunction(CustomEquals)
problem_instance.DefineTransitionFunction(CustomTransitionFunction)
problem_instance.DefineFactibilityFunction(CustomFactibilityFunction)

mdd_instance = MDD(problem_instance)

print(mdd_instance.GetDecisionDiagram())
print(mdd_instance.GetReduceDecisionDiagram())
print(mdd_instance.PrintDecisionDiagram())
print(mdd_instance.PrintReduceDecisionDiagram())   

# Hay que sacar que problem guarde el valor del arco, eso solo estara cuando haya función objetivo 