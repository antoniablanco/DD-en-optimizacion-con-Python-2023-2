from collections import deque

from Class.DDStructure.Graph import Graph
from Class.DDStructure.Node import Node
from Class.DDStructure.Arc import Arc


class LinearObjective:
    '''
    Clase que implementa el algoritmo de Dijkstra para resolver un problema
    de camino mínimo en un grafo dirigido acíclico con pesos lineales.
    '''

    def __init__(self, weights: list, objective: str):
        '''
        Constructor de la clase LinearObjective.

        Parámetros:
        - weights (list): Lista de pesos utilizados en el algoritmo.
        - objective (str): Objetivo del problema ("max" para maximizar, "min" para minimizar).
        '''
        self._weights = weights

        self._visited_nodes = []
        self._unvisited_nodes = []

        self._objective = objective
        self._choose_transform_weights()

    def _choose_transform_weights(self) -> None:
        '''
        Si el objetivo es "max", la función transforma cada peso en la lista de pesos
        multiplicándolo por -1, de modo que el problema de maximización se convierte
        en un problema de minimización.

        Nota: Esta transformación es específica para el algoritmo de Dijkstra.

        '''
    
        if self._objective == "max":
            self._weights = [-weight for weight in self._weights]

    def assign_graph(self, graph: Graph) -> None:
        '''
        Asigna el grafo al que se aplicará el algoritmo.

        Parámetros:
        - graph (Graph): Grafo en el que se aplicará el algoritmo.
        '''
        self._graph = graph
        self._assing_terminal_node_id(graph.structure[-1][0])

    def _assing_terminal_node_id(self, terminal_node: Node) -> None:
        self._terminal_node = terminal_node

    def resolve_graph(self) -> None:
        '''
        Implementa el algoritmo de Dijkstra desde el nodo raíz.

        Parámetros:
        - root_node (Node): Nodo raíz desde el cual se inicia el algoritmo.
        '''
        next_node = self._graph.structure[0][0]
        next_node.update_weight(0)
        self._unvisited_nodes.append(next_node)
        while next_node.id_node != self._terminal_node.id_node:
            self._update_lists(next_node)
            next_node = self._find_minimum_node()

        self._print_inverse_route(next_node)
    
    def _update_lists(self, next_node: Node) -> None:
        '''
        Actualiza las listas de nodos visitados y no visitados.

        Parámetros:

        '''
        self._visited_nodes.append(next_node)
        self._unvisited_nodes.remove(next_node)
        self._update_unvisited_nodes(next_node)
    
    def _find_minimum_node(self) -> None:
        '''
        Encuentra el nodo con menor peso en la lista de nodos no visitados.
        '''

        next_node = self._unvisited_nodes[0]
        best_value = float('inf')
        for node in self._unvisited_nodes:
            node_level = self._get_node_level(node)
            for arc in node.out_arcs:
                transition_value = self._get_arc_transition_value(arc, node_level)
                if transition_value < best_value:
                    best_value = transition_value
                    next_node = node
        return next_node
    
    def _get_node_level(self, node: Node) -> None:
        '''
        Retorna el nivel en el que se encuentra un nodo en el grafo.
        '''
        for level in range(0, len(self._graph.structure)):
            if node in self._graph.structure[level]:
                return level
    
    def _get_arc_transition_value(self, arc: Arc, level: int) -> None:
        '''
        Retorna el valor de transición de un arco.
        '''
        return self._weights[level] * arc.variable_value
    
    def _print_inverse_route(self, terminal_node: Node) -> None:
        '''
        Imprime la mejor ruta encontrada por el algoritmo de Dijkstra.

        Parámetros:
        - terminal_node (Node): Nodo terminal del grafo.
        '''
        current_node = terminal_node
        route = deque()
        while current_node != None:
            if self._objective == "max":
                route.appendleft((current_node.id_node, -current_node.weight))
            else:
                route.appendleft((current_node.id_node, current_node.weight))
            current_node = current_node.parent
        
        self._print_best_weight_route(terminal_node.weight, route)
    
    def _print_best_weight_route(self, weight: int, route: str) -> None:
        '''
        Imprime la mejor ruta encontrada por el algoritmo de Dijkstra.

        Parámetros:
        - weight (int): Peso de la mejor ruta encontrada.
        - route (str): Ruta encontrada por el algoritmo de Dijkstra.
        '''
        print()
        print("Best Route:"," -> ".join(map(str, route)))
        if self._objective == "max":
            print("Weight: " + str(-weight))
        else:
            print("Weight: " + str(weight))

    def _update_unvisited_nodes(self, next_node: Node) -> None:
        '''
        Actualiza la lista de nodos no visitados, y actualiza los pesos de los nodos si es que 
        existe un mejor camino.

        Parámetros:
        - next_node (Node): Nodo que se acaba de visitar.
        '''
        node_level = self._get_node_level(next_node)
        for arc in next_node.out_arcs:
            node = arc.in_node
            transition_value = self._get_arc_transition_value(arc, node_level)
            if arc.in_node not in self._visited_nodes and arc.in_node not in self._unvisited_nodes:
                self._update_node(node, next_node, transition_value)
                self._unvisited_nodes.append(node)
            elif node.weight > next_node.weight + transition_value:
                self._update_node(node, next_node, transition_value)
                self._unvisited_nodes.append(node)

    def _update_node(self, node:Node, next_node: Node, transition_value: int) -> None:
        '''
        Actualiza el peso y el padre de un nodo.

        Parámetros:
        - node (Node): Nodo que se va a actualizar.
        - next_node (Node): Nodo que se acaba de visitar.
        - transition_value (int): Valor de transición del arco que conecta el nodo actual con el nodo que se acaba de visitar.
        '''

        node.update_weight(next_node.weight + transition_value)
        node.update_parent(next_node)

    