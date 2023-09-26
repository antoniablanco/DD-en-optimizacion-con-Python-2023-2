from Class.Node import Node
from Class.Arc import Arc
from Class.Graph import Graph
import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network

class Print():
    def __init__(self, graph):
        self.graph = graph
        self.G = nx.Graph()
        self.net = Network()
        self.domain = []

    def print_graph_G(self):
        self.add_nodes_and_arcs_G()
        pos = self.get_pos_for_nodes()
        #self.add_edge_style_to_graph()
        edge_color = self.add_edge_colors_to_graph()
        nx.draw(self.G, pos=pos, with_labels=True, node_size=500, node_color='lightblue', font_size=12, font_color='black', edge_color=edge_color)

        plt.show()
    

    def add_nodes_and_arcs_G(self):
        for self.graph.layer in self.graph.structure:
            for node in self.graph.layer:
                self.G.add_node(node.id_node)
                for arc in node.in_arcs:
                    self.G.add_edge(arc.out_node.id_node, arc.in_node.id_node, style='dashed', label=arc.variable_value)
                    if arc.variable_value not in self.domain:
                        self.domain.append(arc.variable_value)
    
    def get_pos_for_nodes(self):
        pos = {}
        x = 0
        constante = 1
        for layer_index, layer in enumerate(self.graph.structure):
            x = (-len(layer) * constante)/2
            for node_index, node in enumerate(layer):
                pos[node.id_node] = (x, -layer_index * 100)  # Ajusta las coordenadas x e y según tus necesidades
                x += constante  # Aumenta la coordenada x para separar los nodos en el mismo nivel

        return pos
    
    def add_edge_colors_to_graph(self):  # Cambiar el nombre de la función
        edge_colors = []  # Lista de colores para las aristas
        unique_edge_types = list(set(self.domain))  # Obtener los tipos de aristas únicos

        # Asignar un color a cada tipo de arista
        color_map = plt.cm.get_cmap('viridis', len(unique_edge_types))

        for edge_type in self.domain:
            color_index = unique_edge_types.index(edge_type)
            color = color_map(color_index)
            edge_colors.append(color)
        
        return edge_colors
    
    def add_edge_style_to_graph(self):
        lines_types = ['solid', 'dotted', 'dashed', 'dashdot', 'DashedDotDot', 'Dashed Thick', 'Dotted Thick', 'DashedDotted Thick', 'DashedDottedDotted Thick']

        for u, v, data in self.G.edges(data=True):
            edge_type = data.get("edge_type")
            if edge_type in self.domain:
                index = self.domain.index(edge_type)
                style = lines_types[index % len(lines_types)]
                self.G[u][v]["style"] = style
