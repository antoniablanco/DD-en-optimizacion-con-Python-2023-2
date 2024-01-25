from Class.DDBuilder.DDBuilder import DDBuilder
from Class.ReduceDDBuilder.ReduceDDBuilder import ReduceDDBuilder
from Class.RestrictedDDBuilder.RestrictedDDBuilder import RestrictedDDBuilder
from Class.RelaxedDDBuilder.RelaxedDDBuilder import RelaxedDDBuilder
from Class.GraphVisualization.Print import Print
from Class.GraphVisualization.GraphFile import GraphFile
import copy
import time

from Class.decorators.timer import timing_decorator

class DD():
    '''
    Clase DD (Decision Diagram) para la creación y manipulación de diagramas de decisión.
    '''
    def __init__(self, problem, verbose=False):
        '''
        Constructor de la clase DD.

        Parámetros:
        problem: Una instancia de la clase problem, que se utilizará para crear el diagrama de decisión.

        Atributos:
        - problem: Una instancia de la clase problem, que se utilizará para crear el diagrama de decisión.
        - graph_DD: El diagrama de decisión creado, que se actualiza al generar el diagrama reducido o relajado.
        '''
        self.dd_builder_time = 0
        self.reduce_dd_builder_time = 0
        self.restricted_dd_builder_time = 0
        self.relaxed_dd_builder_time = 0

        self.problem = problem
        self.graph_DD = self._create_decision_diagram(verbose)

    @timing_decorator(enabled=False)
    def _create_decision_diagram(self, verbose):
        print("")
        print("Iniciando la creación del diagrama de decision ...")
        start_time = time.time()  
        self.dd_builder = DDBuilder(self.problem)
        graph = self.dd_builder.get_decision_diagram(verbose)
        end_time = time.time()  
        self.dd_builder_time = end_time - start_time

        print(f"Diagrama de decision creado")
        return graph
    
    @timing_decorator(enabled=False)
    def create_reduce_decision_diagram(self, verbose=False):
        print("")
        print("Iniciando la reducción del diagrama de decision ...")
        start_time = time.time()
        self.reduce_dd_builder = ReduceDDBuilder(self.graph_DD)
        self.graph_DD = self.reduce_dd_builder.get_reduce_decision_diagram(verbose)
        end_time = time.time() 
        self.reduce_dd_builder_time = end_time - start_time
        print(f"Reduccion del diagrama de decision terminada")
    
    @timing_decorator(enabled=False)
    def create_restricted_decision_diagram(self, max_width, verbose=False):
        print("")
        print("Iniciando la creación del diagrama de decision restringido...")
        start_time = time.time()  
        self.restricted_dd_builder = RestrictedDDBuilder(self.problem, max_width)
        self.graph_DD = self.restricted_dd_builder.get_decision_diagram(verbose)
        end_time = time.time()  
        self.restricted_dd_builder_time = end_time - start_time
        print(f"Creación del diagrama de decision restringido terminado")
    
    @timing_decorator(enabled=False)
    def create_relaxed_decision_diagram(self, max_width, verbose=False):
        print("")
        print("Iniciando la creación del diagrama de decision relajado...")
        start_time = time.time()  
        self.relaxed_dd_builder = RelaxedDDBuilder(self.problem, max_width)
        self.graph_DD = self.relaxed_dd_builder.get_decision_diagram(verbose)
        end_time = time.time()  
        self.relaxed_dd_builder_time = end_time - start_time
        print(f"Creación del diagrama de decision relajado terminado")

    def print_decision_diagram(self):
        '''
        NOTA: Este método es solo para fines de prueba, y es importante tener en cuenta que posee 
        máximo 4 tipos de lineas diferente.
        '''
        print_instance = Print(self.graph_DD)
        return print_instance.print_graph_G()

    def export_graph_file(self, file_name):
        '''
        Genera un archivo .GML con el diagrama de decisión actual.

        Parámetros:
        file_name (str): El nombre del archivo Margarita.

        Retorna:
        None
        '''
        GraphFile(file_name, self.graph_DD)

    def get_decision_diagram_graph(self):
        ''' Retorna un objeto de la clase Graph. '''
        return self.graph_DD

    def get_decision_diagram_graph_copy(self):
        ''' Retorna una copia del objeto de la clase Graph, que no posee un
        puntero al mismo objeto. '''
        return copy.deepcopy(self.graph_DD)
    
    def get_DDBuilder_time(self):
        ''' Retorna el tiempo de ejecución del DDBuilder. '''
        return self.dd_builder_time

    def get_reduce_constructor_time(self):
        ''' Retorna el tiempo de ejecución del reduce constructor. '''
        return self.reduce_dd_builder_time
    
    def get_restricted_constructor_time(self):
        ''' Retorna el tiempo de ejecución del restricted constructor. '''
        return self.restricted_dd_builder_time
    
    def get_relaxed_constructor_time(self):
        ''' Retorna el tiempo de ejecución del restricted constructor. '''
        return self.relaxed_dd_builder_time

