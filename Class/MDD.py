from Class.Constructor import Constructor

class MDD():

    def __init__(self, problem):
        self.problem = problem

    def get_decision_diagram(self):
        self.constructor = Constructor(self.problem)
        self.constructor.get_decision_diagram()
        return "Este es mi método  para GetDecisionDiagram"
    
    def get_reduce_decision_diagram(self):
        return "Este es mi método  para GetReduceDecisionDiagram"
    
    def print_decision_diagram(self):
        return "Imprimiendo diagrama de decision"

    def print_reduce_decision_diagram(self):
        return "Imprimiendo diagrama de decision reducido"
