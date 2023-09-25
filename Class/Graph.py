class Graph():

    def __init__(self, initialNode):
        self.nodes = []
        self.structure = [[initialNode]]
        self.actualLayer = 0
    
    def add_node(self, node):
        if node not in self.nodes:
            self.structure[self.actualLayer].append(node)
            self.nodes.append(node)
    
    def new_layer(self):
        self.structure.append([])
        self.actualLayer += 1

    def remove_node(self, node):
        if node in self.nodes:
            self.nodes.remove(node)

            for layer in self.structure:
                if node in layer:
                    layer.remove(node)
                    break

    def get_index_node(self, nodeBuscado):
        index_node = None
        index_layer = None
        for layer in self.structure:
            for node in layer:
                if node is nodeBuscado:
                    index_node = layer.index(nodeBuscado)
                    index_layer = self.structure.index(layer)
                    break
        return (index_node, index_layer)