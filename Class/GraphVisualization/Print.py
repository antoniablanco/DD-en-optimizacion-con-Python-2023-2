import networkx as nx
import matplotlib.pyplot as plt

from Class.Structure.Graph import Graph
from Class.Structure.Node import Node
from Class.Structure.Arc import Arc



class Print():
    '''
    Clase que imprime la representación visual de un grafo utilizando NetworkX y Matplotlib.
    '''

    def __init__(self, graph: Graph):
        '''
        Constructor de la clase Print.

        Parámetros:
        - graph: Grafo que se imprimirá.
        '''
        self._graph = graph
        self._G = nx.MultiGraph()
        self._domain = []

    def print_graph_G(self):
        '''
        Función publica que imprime el grafo utilizando Matplotlib y NetworkX.
        '''
        self._add_nodes_to_G()
        pos = self._get_pos_for_nodes()

        self._add_edges_to_graph(pos)
        self._add_nodes_to_graph(pos)
        
        plt.axis('off')
        plt.show()
    
    def _add_nodes_to_G(self):
        '''
        Agrega nodos al objeto MultiGraph de NetworkX.
        '''
        for self._graph.layer in self._graph.structure:
            for node in self._graph.layer:
                self._G.add_node(node.id_node)
                self._add_arcs_to_G(node)
                
    def _add_arcs_to_G(self, node: Node):
        '''
        Agrega arcos y sus propiedades al objeto MultiGraph de NetworkX.

        Parámetros:
        - node: Nodo al que se le agregarán los arcos al objeto MultiGraph.
        '''
        for arc in node.in_arcs:
            if arc.variable_value not in self._domain:
                self._domain.append(arc.variable_value)

            style = self.add_edge_style_to_graph(arc.variable_value)
            self._G.add_edge(arc.out_node.id_node, arc.in_node.id_node, style=style, label=arc.variable_value)
    
    def add_edge_style_to_graph(self, arc_variable_value: int):
        '''
        Asigna estilos de línea a los arcos del grafo visualizado.

        Parámetros:
        - arc_variable_value: Valor asociado al arco.

        Retorna:
        str: Estilo de línea asignado al arco.
        '''
        lines_types = ['dotted', 'solid', 'dashed', 'dashdot']
        style = 'solid'

        if arc_variable_value in self._domain:
            index = self._domain.index(arc_variable_value)
            style = lines_types[index % len(lines_types)]

        return style
    
    def _get_pos_for_nodes(self):
        '''
        Calcula la posición de los nodos en el grafo visualizado.

        Retorna:
        dict: Diccionario que mapea nodos a posiciones en el grafo visualizado.
        '''
        pos = {}
        x = 0
        constante = 1
        for layer_index, layer in enumerate(self._graph.structure):
            x = (-len(layer) * constante)/2
            for node_index, node in enumerate(layer):
                pos[node.id_node] = (x, -layer_index * 100)  
                x += constante  

        return pos
    
    def _add_edges_to_graph(self, pos):
        '''
        Agrega arcos al grafo visualizado.

        Parámetros:
        - pos: Diccionario que mapea nodos a posiciones en el grafo visualizado.
        '''
        for u, v, data in self._G.edges(data=True):
            style = data.get("style", "solid")
            nx.draw_networkx_edges(self._G, pos, edgelist=[(u, v)], style=style)
    
    def _add_nodes_to_graph(self, pos: int):
        '''
        Agrega nodos al grafo visualizado.

        Parámetros:
        - pos: Diccionario que mapea nodos a posiciones en el grafo visualizado.
        '''
        labels = self._define_labels()
        nx.draw_networkx_labels(self._G, pos=pos, labels=None, font_size=12, font_color='black', verticalalignment='center')
        nx.draw_networkx_labels(self._G, pos=pos, labels=labels, font_size=12, font_color='black', horizontalalignment='left', verticalalignment='center')
        
        nx.draw_networkx_nodes(self._G, pos, node_size=500, node_color='lightblue')
    
    def _define_labels(self):
        '''
        Define etiquetas para los nodos del grafo visualizado.

        Retorna:
        dict: Diccionario que mapea nodos a etiquetas.
        '''
        labels = {}

        for layer in self._graph.structure:
            for node in layer:
                node_id = node.id_node
                labels[node_id] = "    "+str(node.state)
        
        return labels






