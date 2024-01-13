from Class.ObjectiveFunction.LinearObjective import LinearObjective
from Class.ObjectiveFunction.LinearObjectiveDP import LinearObjectiveDP
from Class.ObjectiveFunction.SchedullingObjective import SchedullingObjective

import time

from Exceptions.MyExceptions import MissingObjectiveFunction
from Class.DD import DD
from Class.decorators.timer import timing_decorator

class ObjectiveFunction():
    '''
    Clase DD ObjectiveFunction para la asignación de funciones objetivos y la obtención de un 
    óptimo para un diagrama de decisión.
    '''
    
    def __init__(self, DD: DD):
        '''
        Constructor de la clase ObjectiveFunction.

        Parámetros:
        graphDD (Graph): Diagrama de decisión que se resolverá.
        '''

        self.graph_DD = DD.get_decision_diagram_graph()
        self.time = 0
    
    @timing_decorator(enabled=False)
    def set_objective(self, objective_function):
        '''
        Guarda la información necesaria para tener una función objetivo.

        Parámetros:
        weights (list): Pesos para las variables del problema.
        objective (str): Tipo de objetivo (por ejemplo, "min" o "max").
        '''
        self.minmax = objective_function
        self.minmax.assign_graph(self.graph_DD)
    
    @timing_decorator(enabled=False)
    def solve_dd(self):
        '''
        Resuelve el diagrama de decisión, obteniendo la mejor solución para la función objetivo
        entregada en develop_solver.
        '''

        self._check_if_objective_is_set()
        start_time = time.time()
        self.minmax.resolve_graph()
        end_time = time.time() 
        self.time = end_time - start_time
    
    def get_time(self):
        ''' Retorna el tiempo de ejecución del algoritmo de resolucion. '''
        return self.time
    
    def _check_if_objective_is_set(self) -> None:
        '''
        Verifica que la función objetivo esté definida.
        '''
        if not hasattr(self, "minmax"):
            raise MissingObjectiveFunction()