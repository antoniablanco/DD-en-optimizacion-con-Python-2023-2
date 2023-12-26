from Class.DDBuilder.AbstractDDBuilder import AbstractDDBuilder

class RelaxedDDBuilder(AbstractDDBuilder):
    '''
    Clase que construye un grafo de decisión relajado basado en un problema dado.
    '''

    def __init__(self, problem, max_width):
        super().__init__(problem)
        self._max_width = max_width
    
    def _specific_layer_function(self):
        self._merge_nodes_when_width_is_greater_than_w()

    def _specific_final_function(self):
        self._adjust_node_number()
    
    def _merge_nodes_when_width_is_greater_than_w(self):
        '''
        Realiza la fusión de nodos cuando el ancho es mayor que w.
        '''
        while self._width_is_greater_than_w():
            ordered_nodes = sorted(self.graph.structure[-1], 
            key=lambda node: self._problem.sort_key_nodes_to_merge(node.id_node))
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
        - node_one: Primer nodo a fusionar.
        - node_two: Segundo nodo a fusionar.
        '''

        self._redirect_in_arcs(node_to_remove, node_to_keep)
        self._change_new_state(node_to_remove, node_to_keep)
        self._delete_node(node_to_remove)
    
    def _redirect_in_arcs(self, node_to_remove, node_to_keep):
        '''
        Redirige los arcos de entrada de un nodo al otro nodo.

        Parámetros:
        - changin_nodes_ordered: Lista que contiene nodos en el orden deseado.
        '''
        for arc in node_to_remove.in_arcs:
            arc.in_node = node_to_keep
            if arc not in node_to_keep.in_arcs:
                node_to_keep.add_in_arc(arc)
    
    def _change_new_state(self, node_to_remove, node_to_keep):
        '''
        Cambia el estado del nuevo nodo.
        '''
        node_to_keep.state = self._problem.merge_operator(node_to_remove.state, node_to_keep.state)

    def _delete_node(self, node_to_remove):
        '''
        Elimina un nodo.

        Parámetros:
        - changin_nodes_ordered: Lista que contiene nodos en el orden deseado.
        '''
        self.graph.remove_node(node_to_remove)
        del node_to_remove

    def _adjust_node_number(self):
        '''
        Ajusta el número de nodos en el grafo.
        '''
        initial_node_number = 0
        for layer in self.graph.structure:
            for node in layer:
                node.id_node = str(initial_node_number)
                initial_node_number += 1

    