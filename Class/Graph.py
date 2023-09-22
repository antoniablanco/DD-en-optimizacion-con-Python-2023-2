

class Graph():

    def __init__(self, initialNode):
        self.nodes = []
        self.arcs = []
        self.initialNode = initialNode
        self.finalNode = None
    
    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.append(node)

    def remove_node(self, node):
        if node in self.nodes:
            self.nodes.remove(node)
            self.arcs = [arc for arc in self.arcs if arc.outNode != node and arc.inNode != node]

    def add_arc(self, arc):
        if arc not in self.arcs:
            self.arcs.append(arc)
            self.add_node(arc.outNode)
            self.add_node(arc.inNode)

    def remove_arc(self, arc):
        if arc in self.arcs:
            self.arcs.remove(arc)
            self.remove_node(self.arc.inNode)