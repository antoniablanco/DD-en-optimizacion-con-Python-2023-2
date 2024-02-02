from Class.DDStructure.Graph import Graph
from Class.DDStructure.Node import Node
from Class.DDStructure.Arc import Arc


class LinearObjectiveDP:

    def __init__(self, weights: list, objective: str):
        
        self._weights = weights
        self._objective = objective
    
        self._choose_transform_weights()

    def assign_graph(self, graph: Graph) -> None:
        '''
        Asigna el grafo al que se aplicará el algoritmo.

        Parámetros:
        - graph (Graph): Grafo en el que se aplicará el algoritmo.
        '''
        self._graph = graph

    def _choose_transform_weights(self) -> None:
        '''
        Si el objetivo es "max", la función transforma cada peso en la lista de pesos
        multiplicándolo por -1, de modo que el problema de maximización se convierte
        en un problema de minimización.

        Nota: Esta transformación es específica para el algoritmo utilizado.

        '''
    
        if self._objective == "max":
            self._weights = [-weight for weight in self._weights]
    
    def resolve_graph(self) -> tuple:
        '''
        Se resuelve el grafo a partir de los pesos entragos
        '''

        self.neutro = "neutro"
        self.DP = [[self.neutro, "", []] for i in range(len(self._graph.nodes))]
        
        last_layer_number = len(self._graph.structure) - 2

        value, path, arcs = self.dp(self._graph.nodes[-1], last_layer_number)
        if self._objective == "max":
            value = -value

        return value, path[2:], arcs

    def dp(self, node: Node, layer: int) -> list:
        '''
        Funcion de programacion dinamica para resolver el grafo
        '''
        if len(node.in_arcs) == 0:
            return [0, "", []]
        
        elif self.DP[int(node.id_node)][0] != self.neutro:
            return self.DP[int(node.id_node)]
        
        self.DP[int(node.id_node)] = [float("inf"), "", []]

        for arc in node.in_arcs:
            if self.DP[int(node.id_node)][0] > self.dp(arc.out_node, layer - 1)[0] + arc.variable_value * self._weights[layer]:
                self.DP[int(node.id_node)][0] = self.dp(arc.out_node, layer - 1)[0] + arc.variable_value * self._weights[layer]
                self.DP[int(node.id_node)][1] = self.dp(arc.out_node, layer - 1)[1] + "-> " + str(arc) + "("+str(arc.variable_value)+")"
                self.DP[int(node.id_node)][2] = self.DP[int(arc.out_node.id_node)][2].copy()
                self.DP[int(node.id_node)][2].append(arc)
        return self.DP[int(node.id_node)]

