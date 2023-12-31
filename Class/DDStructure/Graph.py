class Graph():
    '''
    Clase que representa una estructura de grafo con capas de nodos. 
    '''

    def __init__(self, initial_node):
        '''
        Constructor de la clase Graph.

        Parámetros:
        - initial_node(Node): El nodo inicial para el grafo.

        Atributos:
        - nodes (lista): Una lista de todos los nodos en el grafo.
        - structure (lista): Una lista 2D que representa la estructura del grafo en capas.
        - actual_layer (int): El índice de la capa actual que se posee en el grafo.
        '''
        self.nodes = [initial_node]
        self.structure = [[initial_node]]
        self.actual_layer = 0
    
    def __eq__(self, other):
        '''
        Compara si dos objetos de la clase Graph son iguales.

        Parámetros:
        - other (Graph): El otro objeto Graph que se comparará.

        Retorna:
        - bool: True si los objetos son iguales, False en caso contrario.
        '''
        if not isinstance(other, Graph):
            return False
        
        
        devolver = True
        for i, layer in enumerate(self.structure):

            if len(layer) != len(other.structure[i]):
                return False

            for node in layer:
                there_is_equal_node = False
                for other_node in other.structure[i]:
                    if node.state == other_node.state:
                        there_is_equal_node = there_is_equal_node or self._compare_two_nodes(node, other_node)
            devolver = devolver and there_is_equal_node
    
        return devolver
    
    def _compare_two_nodes(self, node1, node2):
        '''
        Verifica entre dos nodos, que sus arcos de entrada y salida sean iguales. Es decir que 
        los arcos posean el mismo valor y provengan/terminen en un nodo con igual estado.
        '''
        devolver_in_arcs = True
        for arc1 in node1.in_arcs:
            there_is_equal_arc = False
            for arc2 in node2.in_arcs:
                if arc1.variable_value == arc2.variable_value and arc1.out_node.state == arc2.out_node.state:
                    there_is_equal_arc = True
            devolver_in_arcs = devolver_in_arcs and there_is_equal_arc
        
        devolver_out_arcs = True
        for arc1 in node1.out_arcs:
            there_is_equal_arc = False
            for arc2 in node2.out_arcs:
                if arc1.variable_value == arc2.variable_value and arc1.in_node.state == arc2.in_node.state:
                    there_is_equal_arc = True
            devolver_out_arcs = devolver_out_arcs and there_is_equal_arc

        return devolver_in_arcs and devolver_out_arcs
    
    def add_node(self, node):
        '''
        Agrega un nodo a la capa actual del grafo.

        Parámetros:
        - node(Node): Objeto de la clase nodo que se agregará a la capa actual.
        '''
        if node not in self.nodes:
            self.structure[self.actual_layer].append(node)
            self.nodes.append(node)
    
    def add_final_node(self, node):
        '''
        Agrega un nodo a la última capa del grafo.

        Parámetros:
        - node(Node): Objeto de la clase nodo que se agregará a la última capa.
        '''
        if node not in self.nodes:
            self.structure[-1].insert(0, node)
            self.nodes.append(node)
    
    def new_layer(self):
        '''Crea una nueva capa en el grafo.'''
        self.structure.append([])
        self.actual_layer += 1
    
    def eliminate_node_and_his_in_arcs(self, node):
        '''
        Elimina un nodo y sus arcos entrantes.

        Parámetros:
        - node(Node): Objeto nodo que se eliminará.
        '''
        for arc in node.in_arcs.copy():
            arc.out_node.out_arcs.remove(arc)
            node.in_arcs.remove(arc)
            del arc
        self.remove_node(node)
        del node

    def remove_node(self, node):
        '''
        Elimina un nodo del grafo.

        Parámetros:
        - node(Node): Objeto nodo que se eliminará del grafo.
        '''
        if node in self.nodes:
            self.nodes.remove(node)
            self._remove_node_from_layer(node)

    def _remove_node_from_layer(self, node):
        '''
        Elimina un nodo de una capa específica.

        Parámetros:
        - node(Node): El objeto nodo que se eliminará de la capa específica.
        '''
        for layer in self.structure:
            if node in layer:
                layer.remove(node)

    