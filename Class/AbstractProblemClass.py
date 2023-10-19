from abc import ABC, abstractmethod


class AbstractProblem(ABC):
    '''
    Esta clase ofrece una interfaz para que los usuarios puedan implementar sus 
    propias clases Problem. Las cuales pueden utilizar con la clase proporcionada MDD 
    para resolver diagramas de decisión.
    '''

    def __init__(self, initial_state, variables):
        '''
        Constructor de la clase AbstractProblem.

        Parámetros:
        - initial_state (NOT DEFINE): El estado inicial del problema, puede ser una lista, int, 
        string, etc. Según lo que se requiera para el problema.
        - variables (list): Una lista que contiene las variables del problema y su dominio, 
        deben seguir el formato List<List<VARIABLE, DOMINIO>> .

        Atributos:
        - initial_state (NOT DEFINE): El estado inicial del problema. 
        - ordered_variables (list): Lista de variables ordenadas.
        - variables_domain (dict): Diccionario que mapea variables a su dominio.
        '''
        self.initial_state = initial_state
        self.ordered_variables = self.get_variables(variables)
        self.variables_domain = self.get_variables_domain(variables)
    
    def get_variables(self, variablesAndDomain):
        variables_ordenadas = []
        for var in variablesAndDomain:
            variables_ordenadas.append(var[0])
        return variables_ordenadas
    
    def get_variables_domain(self, variablesAndDomain):
        variables_domain = {}
        for var in variablesAndDomain:
            variables_domain[var[0]] = var[1]
        return variables_domain

    @abstractmethod
    def equals(self, state_one, state_two):
        '''
        Método abstracto que debe ser implementado por las subclases para determinar si dos estados son iguales.

        Parámetros:
        state_one: El primer estado a comparar.
        state_two: El segundo estado a comparar.

        Retorna:
        bool: True si los estados son iguales, False en caso contrario.
        '''
        pass

    @abstractmethod
    def transition_function(self, previus_state, variable_id, variable_value):
        '''
        Método abstracto que debe ser implementado por las subclases para definir la función de transición.

        Parámetros:
        previus_state: El estado anterior.
        variable_id: El identificador de la variable que se modifica, sigue el mismo type que el entregado en 
        variables.
        variable_value: El valor de la variable que se modifica, es el valor posible de su dominio que se selecciono.

        Retorna:
        tuple: Una tupla que contiene el nuevo estado, siguiente el tipo entregado en inicial_state y un 
        flag, que es True si el estado es factible, y False en caso contrario.
        '''
        pass

    