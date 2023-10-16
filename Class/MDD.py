from Class.Constructor import Constructor
from Class.ReduceConstructor import ReduceConstructor
from Class.Print import Print
from Class.MargaritaFile import MargaritaFile

class MDD():

    def __init__(self, problem):
        self.problem = problem
        self.DD = None
        self.reduceDD = None

    def get_decision_diagram(self):
        self.constructor = Constructor(self.problem)
        self.DD = self.constructor.get_decision_diagram()
        return self.DD
    
    def get_reduce_decision_diagram(self):
        self.reduce_constructor = ReduceConstructor(self.DD)
        self.reduceDD = self.reduce_constructor.get_reduce_decision_diagram()
        return self.reduceDD

    def print_decision_diagram(self):
        print_instance = Print(self.DD)
        return print_instance.print_graph_G()

    def print_reduce_decision_diagram(self):
        print_instance = Print(self.reduceDD)
        return print_instance.print_graph_G()

    def get_margarita_file(self, file_name):
        margarita_file = MargaritaFile(file_name, self.reduceDD)
        return margarita_file.file_name