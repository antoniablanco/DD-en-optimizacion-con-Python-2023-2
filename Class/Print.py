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

    def print_graph_G(self):
        self.add_nodes_and_arcs_G()
        pos = self.get_pos_for_nodes()
        nx.draw(self.G, pos=pos, with_labels=True, node_size=500, node_color='lightblue', font_size=12, font_color='black')

        plt.show()
    
    def add_nodes_and_arcs_G(self):
        for self.graph.layer in self.graph.structure:
            for node in self.graph.layer:
                self.G.add_node(node.id_node)
                for arc in node.in_arcs:
                    self.G.add_edge(arc.out_node.id_node, arc.in_node.id_node)
    
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
