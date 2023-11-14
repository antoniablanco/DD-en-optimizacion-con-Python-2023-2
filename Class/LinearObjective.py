from collections import deque


class LinearObjective:
    '''
    Clase que implementa el algoritmo de Dijkstra para resolver un problema
    de camino mínimo en un grafo dirigido acíclico con pesos lineales.
    '''

    def __init__(self, weights, objective):
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

    def _choose_transform_weights(self):
        '''
        Si el objetivo es "max", la función transforma cada peso en la lista de pesos
        multiplicándolo por -1, de modo que el problema de maximización se convierte
        en un problema de minimización.

        Nota: Esta transformación es específica para el algoritmo de Dijkstra.

        '''
    
        if self._objective == "max":
            self._weights = [-weight for weight in self._weights]

    def assign_graph(self, graph):
        '''
        Asigna el grafo al que se aplicará el algoritmo.

        Parámetros:
        - graph (Graph): Grafo en el que se aplicará el algoritmo.
        '''
        self._graph = graph
        self._assing_terminal_node_id(graph.structure[-1][0])

    def _assing_terminal_node_id(self, terminal_node):
        self._terminal_node = terminal_node

    def _get_arc_transition_value(self, arc, level):
        arc.transition_value = self._weights[level] * arc.variable_value
        return self._weights[level] * arc.variable_value
        
    def dijkstra(self, root_node):
        '''
        Implementa el algoritmo de Dijkstra desde el nodo raíz.

        Parámetros:
        - root_node (Node): Nodo raíz desde el cual se inicia el algoritmo.
        '''
        next_node = root_node
        next_node.update_weight(0)
        self._unvisited_nodes.append(next_node)
        while next_node.id_node != self._terminal_node.id_node:
            self._update_lists(next_node)
            next_node = self._find_minimum_node()

        self._save_results(next_node)

    def _transform_best_weight(self, terminal_node):
        weight = terminal_node.weight
        if self._objective == "max":
            return -weight
        else:
            return weight
        
    def _save_results(self, terminal_node):
       
        self._best_route = self._get_route_of_node(terminal_node)
        weight = terminal_node.weight
        if self._objective == "max":
            self._best_weight =  -weight
        else:
            self._best_weight =  weight

    def _get_route_of_node(self, node):
        current_node = node
        route = deque()
        while current_node != None:
            if self._objective == "max":
                route.appendleft((current_node.id_node, -current_node.weight))
            else:
                route.appendleft((current_node.id_node, current_node.weight))
            current_node = current_node.parent
        route = " -> ".join(map(str, route))
        return route
    
    def get_best_route(self):
        return self._best_route
    
    def get_best_weight(self):
        return self._best_weight

    def _print_best_weight_route(self, weight, route):
        print("Best Route:", self._best_route)
        print("Best Weight:", self._best_weight)
        
    
    def _find_minimum_node(self):
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
    
    def _get_node_level(self, node):
        for level in range(0, len(self._graph.structure)):
            if node in self._graph.structure[level]:
                return level
    
    def _get_arc_transition_value(self, arc, level):
        return self._weights[level] * arc.variable_value
    
    def _print_inverse_route(self, terminal_node):
        current_node = terminal_node
        route = deque()
        while current_node != None:
            if self._objective == "max":
                route.appendleft((current_node.id_node, -current_node.weight))
            else:
                route.appendleft((current_node.id_node, current_node.weight))
            current_node = current_node.parent
        
        self._print_best_weight_route(terminal_node.weight, route)
    
    def _print_best_weight_route(self, weight, route):
        print("Best Route:"," -> ".join(map(str, route)))
        if self._objective == "max":
            print("Weight: " + str(-weight))
        else:
            print("Weight: " + str(weight))

    def _update_unvisited_nodes(self, next_node):
        node_level = self._get_node_level(next_node)
        for arc in next_node.out_arcs:
            if arc.in_node not in self._visited_nodes and arc.in_node not in self._unvisited_nodes:
                node = arc.in_node
                transition_value = self._get_arc_transition_value(arc, node_level)
                node.update_weight(next_node.weight + transition_value)
                node.update_parent(next_node)
                self._unvisited_nodes.append(node)

            else:
                node = arc.in_node
                transition_value = self._get_arc_transition_value(arc, node_level)
                if node.weight > next_node.weight + transition_value:
                    node.update_weight(next_node.weight + transition_value)
                    node.update_parent(next_node)
                    self._unvisited_nodes.append(node)


    