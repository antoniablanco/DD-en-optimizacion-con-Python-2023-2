from Class.DDBuilder.AbstractDDBuilder import AbstractDDBuilder

class RelaxedDDBuilder(AbstractDDBuilder):
    '''
    Clase que construye un grafo de decisión relajado basado en un problema dado.
    '''

    def __init__(self, problem, max_width):
        '''
        Constructor de la clase de diagramas relajados.

        Parámetros:
        - problem: Objeto tipo problema para el cual se construirá el grafo.
        - max_width: Ancho máximo permitido para el grafo.
        '''
        super().__init__(problem)
        self._max_width = max_width
    
    def _specific_layer_function(self):
        '''
        Función a aplicar en cada capa, especifica de esta clase. Se llama a la función que 
        realiza la decisión de fusionar nodos cuando el ancho del grafo es mayor que el especificado
        '''
        self._merge_nodes_when_width_is_greater_than_w() 

    def _specific_final_function(self):
        '''
        Función a aplicar en la última capa, especifica de esta clase. Se llama a la función que 
        actualiza el número de nodos.
        '''
        self._adjust_node_id_number()
    
    def _merge_nodes_when_width_is_greater_than_w(self):
        '''
        Realiza la fusión de nodos cuando el ancho es mayor que w.
        '''
        while self._width_is_greater_than_w():
            ordered_nodes = sorted(self.graph.structure[-1], 
            key=lambda node: self._problem.get_priority_for_merge_nodes(node.id_node, node.state),
            reverse=True)
            self._merge_nodes(ordered_nodes[0], ordered_nodes[1])

    def _width_is_greater_than_w(self):
        '''
        Verifica si el ancho del grafo es mayor que el ancho máximo permitido.
        '''
        return len(self.graph.structure[-1]) > self._max_width
    
    def _merge_nodes(self, node_to_remove, node_to_keep):
        '''
        Fusiona dos nodos.

        Parámetros:
        - node_to_remove: Nodo que será eliminado.
        - node_to_keep: Nodo que se mantendrá.
        '''
        new_state = self._problem.merge_operator(node_to_remove.state, node_to_keep.state)
        exist_node, same_state_node = self._exist_node_with_same_state(new_state)
        if exist_node and (same_state_node!=node_to_keep) and (same_state_node!=node_to_remove):
            self. _merge_with_an_existing_node(node_to_remove, node_to_keep, same_state_node)
        else:
            self._merge_when_doesnt_exist_node(node_to_remove, node_to_keep, new_state)
    
    def _merge_with_an_existing_node(self, node_one, node_two, exist_node):
        '''
        Realiza la fusión de dos nodos con uno ya existente.

        Parámetros:
        - node_one: First node to merge.
        - node_two: Second node to merge.
        - exist_node: Node that already exists.
        '''
        
        self._redirect_in_arcs(node_one, exist_node)
        self._redirect_in_arcs(node_two, exist_node)
        self._delete_node(node_one)
        self._delete_node(node_two)
    
    def _merge_when_doesnt_exist_node(self, node_to_remove, node_to_keep, new_state):
        '''
        Realiza la fusión de dos nodos cuando no existe un nodo con el mismo estado.

        Parámetros:
        - node_to_remove: Nodo que será eliminado.
        - node_to_keep: Nodo que se mantendrá.
        '''
        self._change_new_state(node_to_keep, new_state)
        self._redirect_in_arcs(node_to_remove, node_to_keep)
        self._delete_node(node_to_remove)
    
    def _redirect_in_arcs(self, node_to_remove, node_to_keep):
        '''
        Redirige los arcos de entrada de un nodo al otro nodo.

        Parámetros:
        - node_to_remove: Nodo que será eliminado.
        - node_to_keep: Nodo que se mantendrá.
        '''
        for arc in node_to_remove.in_arcs:
            arc.in_node = node_to_keep
            if arc not in node_to_keep.in_arcs:
                node_to_keep.add_in_arc(arc)
    
    def _change_new_state(self, node, new_state):
        '''
        Cambia el estado del nuevo nodo en base a los estados de los nodos juntados.

        Parámetros:
        - node_to_remove: Nodo que será eliminado.
        - node_to_keep: Nodo que se mantendrá.
        '''
        node.state = new_state

    def _delete_node(self, node_to_remove):
        '''
        Elimina un nodo entregado.

        Parámetros:
        - node_to_remove: Nodo que será eliminado.
        '''
        self.graph.remove_node(node_to_remove)
        del node_to_remove

    def _adjust_node_id_number(self):
        '''
        Ajusta el id de los nodos en el grafo.
        '''
        initial_node_number = 0
        for layer in self.graph.structure:
            for node in layer:
                node.id_node = str(initial_node_number)
                initial_node_number += 1

    