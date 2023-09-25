from Class.Constructor import Constructor

class MDD():

    def __init__(self, problem):
        self.problem = problem

    def GetDecisionDiagram(self):
        self.constructor = Constructor(self.problem)
        self.constructor.get_decision_diagram()
        return "Este es mi método  para GetDecisionDiagram"
    
    def GetReduceDecisionDiagram(self):
        return "Este es mi método  para GetReduceDecisionDiagram"
    
    def PrintDecisionDiagram(self):
        return "Imprimiendo diagrama de decision"

    def PrintReduceDecisionDiagram(self):
        return "Imprimiendo diagrama de decision reducido"
