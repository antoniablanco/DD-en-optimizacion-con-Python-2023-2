class Node():

    def __init__(self, idNode, state):
        self.idNode = idNode
        self.state = state
        self.inArcs = []
        self.outArcs = []
    
    def add_in_arc(self, arc):
        if arc not in self.inArcs:
            self.inArcs.append(arc)
    
    def add_out_arc(self, arc):
        if arc not in self.outArcs:
            self.outArcs.append(arc)
    
    def remove_in_arc(self, arc):
        if arc in self.inArcs:
            self.inArcs.remove(arc)

    def remove_out_arc(self, arc):
        if arc in self.outArcs:
            self.outArcs.remove(arc)