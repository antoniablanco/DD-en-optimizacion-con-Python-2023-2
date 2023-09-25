from Class.Problem import Problem
from Class.MDD import MDD

# Creo una instancia de Problem
initialState = [0]
orderedVariables = ['x_1','x_2','x_3','x_4']
variableNature = [0, 1]

problem_instance = Problem(initialState, orderedVariables, variableNature)

def CustomEquals(stateOne, stateTwo):
    return stateOne == stateTwo

def CustomTransitionFunction():
    return "Este es mi método personalizado para TransitionFunction"

def CustomFactibilityFunction(state):
    return int(state[0]) <= 6


# Asociar las funciones a la instancia
#setattr(problem_instance, 'Equals', CustomEquals)
#setattr(problem_instance, 'TransitionFunction', CustomTransitionFunction)
#setattr(problem_instance, 'FactibilityFunction', CustomFactibilityFunction)
problem_instance.DefineEqualsFunction(CustomEquals)
problem_instance.DefineTransitionFunction(CustomTransitionFunction)
problem_instance.DefineFactibilityFunction(CustomFactibilityFunction)

# Crear una instancia de MDD
mdd_instance = MDD(problem_instance)

# Llamar a los metodos personalisados
print(mdd_instance.GetDecisionDiagram())
print(mdd_instance.GetReduceDecisionDiagram())
print(mdd_instance.PrintDecisionDiagram())
print(mdd_instance.PrintReduceDecisionDiagram())   