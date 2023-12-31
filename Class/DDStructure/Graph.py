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
        for i, layer in enumerate(self.structure):
            if len(layer) != len(other.structure[i]):
                return False

            for j in range(len(layer)):
                node1 = layer[j]
                node2 = other.structure[i][j]

                # Compara los atributos de los nodos
                if str(node1.id_node) != str(node2.id_node) or node1.state != node2.state:
                    return False

                # Compara los atributos de los arcos
                arcs1 = node1.in_arcs + node1.out_arcs
                arcs2 = node2.in_arcs + node2.out_arcs

                for arc1, arc2 in zip(arcs1, arcs2):
                    if arc1.variable_value != arc2.variable_value or arc1.variable_id != arc2.variable_id:
                        return False
        return True
    
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

    def remove_node(self, node):
        '''
        Elimina un nodo del grafo.

        Parámetros:
        - node(Node): Objeto nodo que se eliminará.
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

    def get_index_node(self, search_node):
        '''
        Retorna el índice de un nodo específico en el grafo.

        Parámetros:
        - search_node(Node): Objeto nodo que se busca.

        Retorna:
        tuple: Una tupla que contiene el índice del nodo y el índice de la capa.
        '''
        index_node = None
        index_layer = None

        for layer_index, layer in enumerate(self.structure):
            index_in_layer = self._find_node_in_layer(layer, search_node)
            if index_in_layer is not None:
                index_node = index_in_layer
                index_layer = layer_index
                break

        return (index_node, index_layer)

    def _find_node_in_layer(self, layer, search_node):
        '''
        Encuentra un nodo en una capa específica.

        Parámetros:
        - layer(int): La capa en la que se busca el nodo.
        - search_node(Node): El nodo que se busca en la capa.

        Retorna:
        int: El índice del nodo en la capa o None si no se encuentra.
        '''
        for node_index, node in enumerate(layer):
            if node is search_node:
                return node_index

        return None