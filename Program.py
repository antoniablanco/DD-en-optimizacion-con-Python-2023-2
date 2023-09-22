from Class.Problem import Problem

# Creo una instancia de Problem
initialState = [0]
orderedVariables = ['x_1','x_2','x_3','x_4']
variableNature = [0,1]

problem_instance = Problem(initialState, orderedVariables, variableNature)

# Definir un método personalizado para Equals
def Equals():
    return "Este es mi método personalizado para Equals"

# Definir un método personalizado para Equals
def TransitionFunction():
    return "Este es mi método personalizado para TransitionFunction"

# Definir un método personalizado para TransitionFunction
def FactibilityFunction():
    return "Este es mi método personalizado para FactibilityFunction"


# Asociar las funciones a la instancia
problem_instance.Equals = Equals()
problem_instance.TransitionFunction = TransitionFunction()
problem_instance.FactibilityFunction = FactibilityFunction()

# Llamar a los metodos personalisados
print(problem_instance.GetDecisionDiagram())
print(problem_instance.GetReduceDecisionDiagram())
print(problem_instance.PrintDecisionDiagram())
print(problem_instance.PrintReduceDecisionDiagram())   