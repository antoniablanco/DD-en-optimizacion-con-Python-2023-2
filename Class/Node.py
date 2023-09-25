class Node():

    def __init__(self, id_node, state):
        self.id_node = id_node
        self.state = state
        self.in_arcs = []
        self.out_arcs = []
    
    def add_in_arc(self, arc):
        if arc not in self.in_arcs:
            self.in_arcs.append(arc)
    
    def add_out_arc(self, arc):
        if arc not in self.out_arcs:
            self.out_arcs.append(arc)
    
    def remove_in_arc(self, arc):
        if arc in self.in_arcs:
            self.in_arcs.remove(arc)

    def remove_out_arc(self, arc):
        if arc in self.out_arcs:
            self.out_arcs.remove(arc)