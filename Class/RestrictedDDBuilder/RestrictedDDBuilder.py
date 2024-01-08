from Class.DDBuilder.AbstractDDBuilder import AbstractDDBuilder

class RestrictedDDBuilder(AbstractDDBuilder):
    '''
    Clase que construye un grafo de decisión restringido basado en un problema dado.
    '''
    
    def __init__(self, problem, max_width):
        '''
        Constructor de la clase de diagramas restringidos.

        Parámetros:
        - problem: Objeto tipo problema para el cual se construirá el grafo.
        - max_width: Ancho máximo permitido para el grafo.
        '''
        super().__init__(problem)
        self._max_width = max_width
            
    def _specific_layer_function(self):
        '''
        Función a aplicar en cada capa, especifica de esta clase. Se llama a la función que 
        realiza la decisión de eliminar un nodo cuando el ancho del grafo es mayor que el especificado
        '''
        self._eliminate_nodes_when_width_is_greater_than_w()

    def _specific_final_function(self):
        '''
        Función a aplicar en la última capa, especifica de esta clase. 
        Primero llama a la función que elimina aquellos nodos que no poseen arcos salientes, y
        depués se llama a la función que actualiza el número de nodos.
        '''
        self._eliminate_nodes_without_out_arcs()
        self._adjust_node_number()
    
    def _eliminate_nodes_when_width_is_greater_than_w(self):
        '''
        Se realiza la decisión de eliminar nodos cuando el ancho del grafo es mayor que el 
        ancho máximo permitido.
        '''
        if self._width_is_greater_than_w():
            ordered_nodes = sorted(self.graph.structure[-1], key=lambda node: self._problem.get_priority_for_discard_node(
            node.state))
            nodes_to_eliminate = ordered_nodes[self._max_width:] or []
            self._eliminate_nodes(nodes_to_eliminate)
    
    def _width_is_greater_than_w(self):
        '''
        Verifica si el ancho del grafo es mayor que el ancho máximo permitido.
        '''
        return len(self.graph.structure[-1]) > self._max_width

    def _eliminate_nodes(self, nodes_to_eliminate):
        '''
        Elimina los nodos entregados y sus arcos entrantes
        '''
        for node in nodes_to_eliminate:
            self.graph.eliminate_node_and_his_in_arcs(node) 

    def _eliminate_nodes_without_out_arcs(self):
        '''
        Elimina los nodos que no tienen arcos salientes.
        '''
        nodes_in_layers = self.graph.structure[::-1]
        for layer in nodes_in_layers[1:]:
            for node in layer:
                if node.out_arcs == []:
                    self.graph.eliminate_node_and_his_in_arcs(node)

    def _adjust_node_number(self):
        '''
        Ajusta el número de nodos en el grafo.
        '''
        initial_node_number = 0
        for layer in self.graph.structure:
            for node in layer:
                node.id_node = str(initial_node_number)
                initial_node_number += 1

    