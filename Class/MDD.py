from Class.Constructor import Constructor
from Class.Print import Print

class MDD():

    def __init__(self, problem):
        self.problem = problem
        self.DD = None

    def get_decision_diagram(self):
        self.constructor = Constructor(self.problem)
        self.DD = self.constructor.get_decision_diagram()
        return "Este es mi método  para GetDecisionDiagram"
    
    def get_reduce_decision_diagram(self):
        return "Este es mi método  para GetReduceDecisionDiagram"
    
    def print_decision_diagram(self):
        print_instance = Print(self.DD)
        return print_instance.print_graph_G()

    def print_reduce_decision_diagram(self):
        return "Imprimiendo diagrama de decision reducido"
