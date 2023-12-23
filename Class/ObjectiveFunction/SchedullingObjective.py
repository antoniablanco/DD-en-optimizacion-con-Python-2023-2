from Class.DDStructure.Graph import Graph
from Class.DDStructure.Node import Node
from Class.DDStructure.Arc import Arc


class SchedullingObjective:
    '''
    Clase que implementa el algoritmo de earliest completion time para resolver un problema
    de camino mínimo en un grafo dirigido acíclico con pesos dependientes de nodos anteriores.
    '''

    def __init__(self, weights: list, objective: str):
        '''
        Constructor de la clase SchedullingObjective.

        Parámetros:
        - weights (list): Lista de pesos utilizados en el algoritmo.
        - objective (str): Objetivo del problema ("max" para maximizar, "min" para minimizar).
        '''
        self.operation_time = weights[0]
        self.setup_time = weights[1]

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

    def resolve_graph(self, root_node: Node) -> None:
        '''
        Implementa el algoritmo de Earliest Completion Time desde el nodo raíz.

        Parámetros:
        - root_node (Node): Nodo raíz desde el cual se inicia el algoritmo.
        '''
        next_node = root_node
        next_node.update_weight(0)
        self._unvisited_nodes.append(next_node)
        while next_node.id_node != self._terminal_node.id_node:
            self._update_lists(next_node)
            next_node = self._unvisited_nodes[0]

        self._print_best_weight_route(self._terminal_node.weight)

    def _update_lists(self, next_node: Node) -> None:
        '''
        Actualiza las listas de nodos visitados y no visitados.

        '''
        self._visited_nodes.append(next_node)
        self._unvisited_nodes.remove(next_node)
        self._update_unvisited_nodes(next_node)

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
            transition_value = self._get_arc_transition_value(arc)
            if node not in self._visited_nodes and node not in self._unvisited_nodes:
                self._update_node(node, next_node, transition_value)
                self._unvisited_nodes.append(node)
            elif node.weight > transition_value:
                self._update_node(node, next_node, transition_value)

    def _get_node_level(self, node: Node) -> None:
        '''
        Retorna el nivel en el que se encuentra un nodo en el grafo.
        '''
        for level in range(0, len(self._graph.structure)):
            if node in self._graph.structure[level]:
                return level
            
    def _get_arc_transition_value(self, arc: Arc) -> None:
        '''
        Retorna el valor de transición de un arco.
        '''
        id_operacion_actual = int(arc.variable_value)
        nodo_padre = arc.out_node
        tiempos = []
        if nodo_padre.in_arcs == []:
            arc.weight = self._get_operation_time(id_operacion_actual)
            return arc.weight
        for arc2 in nodo_padre.in_arcs:
            tiempo = arc2.weight
            tiempo += self._get_setups_time(int(arc2.variable_value), id_operacion_actual)
            tiempo += self._get_operation_time(id_operacion_actual)
            tiempos.append(tiempo)
        arc.weight = min(tiempos)
        return arc.weight

    def _get_setups_time(self, id_operacion_anterior, id_operacion_actual):
        '''
        Retorna el tiempo de set up entre la operación anterior y la operación actual.

        Parámetros:
        - id_operacion_anterior (int): ID de la operación anterior.
        - id_operacion_actual (int): ID de la operación actual.
        '''
        return self.setup_time[id_operacion_anterior][id_operacion_actual]
    
    def _get_operation_time(self, id_operacion_actual):
        '''
        Retorna el tiempo que se demora en hacr la operación actual.

        Parámetros:
        - id_operacion_actual (int): ID de la operación actual.
        '''
        return self.operation_time[id_operacion_actual]

    def _update_node(self, node:Node, next_node: Node, transition_value: int) -> None:
        '''
        Actualiza el peso y el padre de un nodo.

        Parámetros:
        - node (Node): Nodo que se va a actualizar.
        - next_node (Node): Nodo que se acaba de visitar.
        - transition_value (int): Valor de transición del arco que conecta el nodo actual con el nodo que se acaba de visitar.
        '''
        node.update_weight(transition_value)
        node.update_parent(next_node)

    def _print_best_weight_route(self, weight: int) -> None:
        '''
        Imprime la mejor ruta que encuentra el algoritmo.

        Parámetros:
        - weight (int): Peso de la mejor ruta encontrada.
        '''
        if self._objective == "max":
            print("Weight: " + str(-weight))
        else:
            print("Weight: " + str(weight))