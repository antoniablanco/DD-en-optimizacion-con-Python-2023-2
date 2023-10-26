from Class.LinearObjective import LinearObjective


class ObjectiveFunction():
    '''
    Clase DD ObjectiveFunction para la asignación de funciones objetivos y la obtención de un 
    óptimo para un diagrama de decisión.
    '''
    
    def __init__(self, graphDD):
        self.graph_DD = graphDD
    
    def develop_solver(self, weights, objective="min"):
        '''
        Guarda la información necesaria para tener una función objetivo.

        Parámetros:
        weights (list): Pesos para las variables del problema.
        objective (str): Tipo de objetivo (por ejemplo, "min" o "max").
        '''
        try:
            self.minmax = LinearObjective(weights, objective)
            self.minmax.assign_graph(self.graph_DD)
        except Exception as e:
            print(e)
            raise Exception("Solver not defined")
    
    def solve_dd(self):
        '''
        Resuelve el diagrama de decisión, obteniendo la mejor solución para la función objetivo
        entregada en develop_solver.
        '''
        try:
            self.minmax.dijkstra(self.graph_DD.structure[0][0])
        except Exception as e:
            print(e)
            raise Exception("Solver not defined")