class Graph():

    def __init__(self, initial_node):
        self.nodes = []
        self.structure = [[initial_node]]
        self.actual_layer = 0
    
    def add_node(self, node):
        if node not in self.nodes:
            self.structure[self.actual_layer].append(node)
            self.nodes.append(node)
    
    def add_final_node(self, node):
        if node not in self.nodes:
            self.structure[-1].insert(0, node)
            self.nodes.append(node)
    
    def new_layer(self):
        self.structure.append([])
        self.actual_layer += 1

    def remove_node(self, node):
        if node in self.nodes:
            self.nodes.remove(node)
            self.remove_node_from_layer(node)
    
    def remove_node_from_layer(self, node):
        for layer in self.structure:
                if node in layer:
                    layer.remove(node)

    def get_index_node(self, search_node):
        index_node = None
        index_layer = None

        for layer_index, layer in enumerate(self.structure):
            index_in_layer = self.find_node_in_layer(layer, search_node)
            if index_in_layer is not None:
                index_node = index_in_layer
                index_layer = layer_index
                break

        return (index_node, index_layer)

    def find_node_in_layer(self, layer, search_node):
        for node_index, node in enumerate(layer):
            if node is search_node:
                return node_index

        return None