from Class.Constructor import Constructor
from Class.ReduceConstructor import ReduceConstructor
from Class.Print import Print
from Class.MargaritaFile import MargaritaFile
from Class.MinMaxObjective import MinMaxFunction


class DD():
    '''
    Clase DD (Decision Diagram) para la creación y manipulación de diagramas de decisión.
    '''
    def __init__(self, problem):
        '''
        Constructor de la clase DD.

        Parámetros:
        problem: Una instancia de la clase problem, que se utilizará para crear el diagrama de decisión.

        Atributos:
        - problem: Una instancia de la clase problem, que se utilizará para crear el diagrama de decisión.
        - DD: El diagrama de decisión creado, que se actualiza al generar el diagrama reducido o relajado.
        - objective: El tipo de objetivo (por ejemplo, "min" o "max"). Por defecto es "min".
        '''
        self.problem = problem
        self.DD = self._create_decision_diagram()
        self.objective = 'min'

    def _create_decision_diagram(self):
        print("")
        print("Iniciando la creación del diagrama de decision ...")
        self.constructor = Constructor(self.problem)
        print("Diagrama de decision creado")

        return self.constructor.get_decision_diagram()
    
    def create_reduce_decision_diagram(self):
        print("")
        print("Iniciando la reducción del diagrama de decision ...")
        self.reduce_constructor = ReduceConstructor(self.DD)
        self.DD = self.reduce_constructor.get_reduce_decision_diagram()
        print("Reduccion del diagrama de decision terminada")

    def print_decision_diagram(self):
        print_instance = Print(self.DD)
        return print_instance.print_graph_G()

    def export_margarita_file(self, file_name):
        '''
        Genera un archivo Margarita con el diagrama de decisión actual.

        Parámetros:
        file_name (str): El nombre del archivo Margarita.

        Retorna:
        None
        '''
        MargaritaFile(file_name, self.DD, self.objective)

    def get_decision_diagram_graph(self):
        ''' Retorna un objeto de la clase Graph. '''
        return self.DD

