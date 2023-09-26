import networkx as nx
import matplotlib.pyplot as plt

class Print():
    def __init__(self, graph):
        self.graph = graph
        self.G = nx.MultiGraph()
        self.domain = []

    def print_graph_G(self):
        self.add_nodes_to_G()
        pos = self.get_pos_for_nodes()

        self.add_edges_to_graph(pos)
        self.add_nodes_to_graph(pos)
        
        plt.axis('off')
        plt.show()
    
    def add_nodes_to_graph(self, pos):
        labels = self.define_labels()
        nx.draw_networkx_labels(self.G, pos=pos, labels=None, font_size=12, font_color='black', verticalalignment='center')
        nx.draw_networkx_labels(self.G, pos=pos, labels=labels, font_size=12, font_color='black', horizontalalignment='left', verticalalignment='center')
        
        nx.draw_networkx_nodes(self.G, pos, node_size=500, node_color='lightblue')
    
    def add_edges_to_graph(self, pos):
        for u, v, data in self.G.edges(data=True):
            style = data.get("style", "solid")
            nx.draw_networkx_edges(self.G, pos, edgelist=[(u, v)], style=style)
        
    def define_labels(self):
        labels = {}

        for layer in self.graph.structure:
            for node in layer:
                node_id = node.id_node
                labels[node_id] = "    "+str(node.state)
        
        return labels

    def add_nodes_to_G(self):
        for self.graph.layer in self.graph.structure:
            for node in self.graph.layer:
                self.G.add_node(node.id_node)
                self.add_arcs_to_G(node)

    def add_arcs_to_G(self, node):
        for arc in node.in_arcs:
            if arc.variable_value not in self.domain:
                self.domain.append(arc.variable_value)

            style = self.add_edge_style_to_graph(arc.variable_value)
            self.G.add_edge(arc.out_node.id_node, arc.in_node.id_node, style=style, label=arc.variable_value)
    
    def get_pos_for_nodes(self):
        pos = {}
        x = 0
        constante = 1
        for layer_index, layer in enumerate(self.graph.structure):
            x = (-len(layer) * constante)/2
            for node_index, node in enumerate(layer):
                pos[node.id_node] = (x, -layer_index * 100)  
                x += constante  

        return pos
    
    def add_edge_style_to_graph(self, arc_variable_value):
        lines_types = ['dotted', 'solid', 'dashed', 'dashdot', 'DashedDotDot', 'Dashed Thick', 'Dotted Thick', 'DashedDotted Thick', 'DashedDottedDotted Thick']
        style = 'solid'

        if arc_variable_value in self.domain:
            index = self.domain.index(arc_variable_value)
            style = lines_types[index % len(lines_types)]

        return style






