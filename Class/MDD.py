from Class.Constructor import Constructor
from Class.ReduceConstructor import ReduceConstructor
from Class.Print import Print
from Class.MargaritaFile import MargaritaFile
from Class.MinMaxObjective import MinMaxFunction

class MDD():

    def __init__(self, problem):
        self.problem = problem
        self.DD = None
        self.reduceDD = None
        self.create_decision_diagram()

    def create_decision_diagram(self):
        print("")
        print("Iniciando la creación del diagrama de decision ...")
        self.constructor = Constructor(self.problem)
        self.DD = self.constructor.get_decision_diagram()
        print("Diagrama de decision creado")
    
    def create_reduce_decision_diagram(self):
        print("")
        print("Iniciando la reducción del diagrama de decision ...")
        self.reduce_constructor = ReduceConstructor(self.DD)
        self.DD = self.reduce_constructor.get_reduce_decision_diagram()
        print("Reduccion del diagrama de decision terminada")

    def print_decision_diagram(self):
        print_instance = Print(self.DD)
        return print_instance.print_graph_G()


    def get_margarita_file(self, file_name):
        margarita_file = MargaritaFile(file_name, self.DD)
        return margarita_file.file_name
    
    def develop_solver(self, variable_ranges, function_operations, weights, objective):
        try:
            self.minmax = MinMaxFunction(variable_ranges, function_operations, weights, objective)
            self.minmax.assign_transition_values(self.reduceDD)
        except Exception as e:
            print(e)
            raise Exception("Solver not defined")

    
    def solve_dd(self):
        try:
            self.minmax.anti_dijkstra(self.reduceDD.structure[0][0])
        except Exception as e:
            print(e)
            raise Exception("Solver not defined")
