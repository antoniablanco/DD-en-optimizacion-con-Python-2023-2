from Class.Problem import Problem
from Class.MDD import MDD

# Creo una instancia de Problem
initialState = [0]
orderedVariables = ['x_1','x_2','x_3','x_4']
variableNature = [0, 1]

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

# Crear una instancia de MDD
mdd_instance = MDD(problem_instance)

# Llamar a los metodos personalisados
print(mdd_instance.GetDecisionDiagram())
print(mdd_instance.GetReduceDecisionDiagram())
print(mdd_instance.PrintDecisionDiagram())
print(mdd_instance.PrintReduceDecisionDiagram())   