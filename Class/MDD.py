from Class.Constructor import Constructor
from Class.ReduceConstructor import ReduceConstructor
from Class.Print import Print
from Class.MargaritaFile import MargaritaFile
from Class.MinMaxObjective import MinMaxFunction


class MDD():
    '''
    Clase MDD (Multi-Valued Decision Diagram) para la creación y manipulación de diagramas de decisión.
    '''
    def __init__(self, problem):
        '''
        Constructor de la clase MDD.

        Parámetros:
        problem: Una instancia de la clase problem, que se utilizará para crear el diagrama de decisión.

        Atributos:
        - problem: Una instancia de la clase problem, que se utilizará para crear el diagrama de decisión.
        - DD: El diagrama de decisión creado, que se actualiza al generar el diagrama reducido o relajado.
        '''
        self.problem = problem
        self.DD = None
        self.create_decision_diagram()

    def create_decision_diagram(self):
        '''
        Crea el diagrama de decisión utilizando el problema proporcionado y lo guarda en self.DD.
        '''
        print("")
        print("Iniciando la creación del diagrama de decision ...")
        self.constructor = Constructor(self.problem)
        self.DD = self.constructor.get_decision_diagram()
        print("Diagrama de decision creado")
    
    def create_reduce_decision_diagram(self):
        '''
        Reduce el diagrama de decisión y lo guarda en self.DD.
        '''
        print("")
        print("Iniciando la reducción del diagrama de decision ...")
        self.reduce_constructor = ReduceConstructor(self.DD)
        self.DD = self.reduce_constructor.get_reduce_decision_diagram()
        print("Reduccion del diagrama de decision terminada")

    def print_decision_diagram(self):
        print_instance = Print(self.DD)
        return print_instance.print_graph_G()


    def get_margarita_file(self, file_name):
        '''
        Obtiene un archivo Margarita para el diagrama de decisión.

        Parámetros:
        file_name (str): El nombre del archivo Margarita.

        Retorna:
        str: El nombre del archivo Margarita generado.
        '''
        margarita_file = MargaritaFile(file_name, self.DD)
        return margarita_file.file_name
    
    def develop_solver(self, variable_ranges, function_operations, weights, objective):
        '''
        Guarda la información necesaria para tener una función objetivo.

        Parámetros:
        variable_ranges (list): Rangos de las variables del problema.
        function_operations (list): Operaciones a aplicar en la función objetivo.
        weights (list): Pesos para las variables del problema.
        objective (str): Tipo de objetivo (por ejemplo, "min" o "max").
        '''
        try:
            self.minmax = MinMaxFunction(variable_ranges, function_operations, weights, objective)
            self.minmax.assign_transition_values(self.reduceDD)
        except Exception as e:
            print(e)
            raise Exception("Solver not defined")
    
    def solve_dd(self):
        '''
        Resuelve el diagrama de decisión, obteniendo la mejor solución para la función objeitivo
        entregada en develop_solver.
        '''
        try:
            self.minmax.anti_dijkstra(self.reduceDD.structure[0][0])
        except Exception as e:
            print(e)
            raise Exception("Solver not defined")
