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

        Retorna:
        float: El valor de la mejor solución.
        '''
        try:
            print("Resolviendo diagrama de decisión...")
            self.minmax.dijkstra(self.graph_DD.structure[0][0])
            print("Diagrama de decisión resuelto")
        except Exception as e:
            print(e)
            raise Exception("Solver not defined")
        
    def get_best_route(self):
        '''
        Retorna la ruta que lleva a la mejor solución.

        Retorna:
        str: representación de ruta donde cada variable es una tupla, siendo el primer valor el nodo
        elegido, y el segundo valor el peso hasta ese momento.
        '''
        try:
            return self.minmax.get_best_route()
        except Exception as e:
            print(e)
            raise Exception("Could not obtain best route")
        
    def get_best_solution(self):
        '''
        Retorna el valor de la mejor solución.

        Retorna:
        int: valor de la mejor solución.
        '''
        try:
            return self.minmax.get_best_weight()
        except Exception as e:
            print(e)
            raise Exception("Could not obtain best solution")