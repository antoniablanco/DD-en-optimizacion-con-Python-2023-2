from Class.DDStructure.Node import Node
from Class.DDStructure.Arc import Arc
from Class.DDStructure.Graph import Graph

import copy


class ReduceDDBuilder():
    '''
    Clase que implementa un algoritmo para la reducción de un grafo de decisión.
    '''

    def __init__(self, graph):
        '''
        Constructor de la clase ReduceConstructor.

        Parámetros:
        - graph (Graph): El grafo de decisión a reducir.
        '''
        self._graph = copy.deepcopy(graph)
        self._layerWorking = self._graph.actual_layer
    
    def get_reduce_decision_diagram(self, should_visualize):
        '''
        Realiza la reducción del grafo de decisión y lo entrega.

        Parámetros:
        - should_visualize (bool): Indica si se debe visualizar el grafo durante el proceso.

        Retorna:
        - Graph: El grafo de decisión reducido.
        '''
        for layer in reversed(self._graph.structure[:-1]):
            self._print_graph(should_visualize)
            self._layerWorking -= 1 
            self._reviewing_layer(layer)

        self._final_layer_set_up()
        self._print_graph(should_visualize)
                
        return self._graph
    
    def _print_graph(self, should_visualize):
        '''
        Imprime el grafo si se solicita la visualización.

        Parámetros:
        - should_visualize (bool): Indica si se debe visualizar el grafo.
        '''
        if should_visualize:
            self._print()

    def _print(self):
        '''
        Imprime el contenido de cada capa del grafo.
        '''
        print("")
        for layer in self._graph.structure:
            print("------------------------------------------------------")
            for node in layer:
                in_arcs_str = ", ".join(str(arc) for arc in node.in_arcs) 
                print(str(node) + "(" + in_arcs_str + ")", end=" ")
            print("")
    
    def _reviewing_layer(self, layer):
        '''
        Revisa la capa actual para fusionar nodos que cumplen con llegar al mismo nodo posteriormente
        con el mismo valor de la variable.

        Parámetros:
        - layer: Lista de nodos en la capa actual.
        '''
        for i, node_one in enumerate(layer):
            nodes = layer[i+1:]

            while len(nodes) > 0:
                node_two = nodes.pop(0)
                if self._checking_if_two_nodes_should_merge(node_one, node_two):
                    self._merge_nodes(node_one, node_two)
    
    def _checking_if_two_nodes_should_merge(self, node_one, node_two):
        '''
        Verifica si dos nodos deberían fusionarse.

        Parámetros:
        - node_one: Primer nodo a comparar.
        - node_two: Segundo nodo a comparar.

        Retorna:
        bool: True si los nodos deben fusionarse, False en caso contrario.
        '''
        PathsOfNodeOne = self._get_node_of_every_type_of_path(node_one)
        PathsOfNodeTwo = self._get_node_of_every_type_of_path(node_two)
        return PathsOfNodeOne == PathsOfNodeTwo

    def _get_node_of_every_type_of_path(self, node):
        '''
        Obtiene los nodos del camino de un nodo.

        Parámetros:
        - node: Nodo para el cual se obtienen los nodos del camino.

        Retorna:
        dict: Un diccionario que contiene nodos del camino como claves y valores de las variables como valores.
        '''
        NodesOfPath = []
        for arc in node.out_arcs:
            NodesOfPath.append(str(arc.in_node)+"_"+str(arc.variable_value))
        return NodesOfPath

    def _merge_nodes(self, node_one, node_two):
        '''
        Fusiona dos nodos.

        Parámetros:
        - node_one: Primer nodo a fusionar.
        - node_two: Segundo nodo a fusionar.
        '''
        node_to_remove, node_to_keep = list(self._get_order_of_changin_nodes(node_one, node_two))
        
        self._redirect_in_arcs(node_to_remove, node_to_keep)
        self._delete_out_arcs(node_to_remove)
        self._delete_node(node_to_remove)
    
    def _get_order_of_changin_nodes(self, node_one, node_two):
        '''
        Obtiene el orden de cambio de nodos.

        Parámetros:
        - node_one: Primer nodo a comparar.
        - node_two: Segundo nodo a comparar.

        Retorna:
        tuple: Tupla que contiene el orden de cambio de nodos, primero va el nodo que se elimina
        y en segunfa posición el que se mantiene.
        '''
        current_layer = self._graph.structure[self._layerWorking]
        if node_one in current_layer and node_two in current_layer:
            if current_layer.index(node_one) > current_layer.index(node_two):
                return node_one, node_two 
            else:
                return node_two, node_one
        else:
            print("Error: No se encuentran los nodos en la capa actual")
    
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
    
    def _delete_out_arcs(self, node_to_remove):
        '''
        Elimina los arcos de salida de un nodo.

        Parámetros:
        - changin_nodes_ordered: Lista que contiene nodos en el orden deseado.
        '''
        for arc in node_to_remove.out_arcs:
            node_to_remove.out_arcs.remove(arc)
            arc.in_node.in_arcs.remove(arc)
            del arc                
    
    def _delete_node(self, node_to_remove):
        '''
        Elimina un nodo.

        Parámetros:
        - changin_nodes_ordered: Lista que contiene nodos en el orden deseado.
        '''
        self._graph.remove_node(node_to_remove)
        del node_to_remove
    
    def _final_layer_set_up(self):
        '''
        Configura la última capa del grafo después de la reducción.
        '''
        self._update_node_names()

    def _update_node_names(self):
        '''
        Actualiza los nombres de los nodos en el grafo.
        '''
        valor_actual = 1

        for layer in self._graph.structure[1:]:
            for node in layer:
                if node.id_node!='t':
                    node.id_node = str(valor_actual)
                    valor_actual += 1
    

        
