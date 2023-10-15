from collections import deque

class MinMaxFunction:

    # def __init__(self, n_variables, variable_ranges, function_operations, weights, graph):
    def __init__(self, objective):
        # self.n_variables = n_variables
        # self.variable_ranges = variable_ranges
        # self.function_operations = function_operations
        # self.weights = weights

        self.visited_nodes = []
        self.unvisited_nodes = []
        self.objective_function = self.choose_objective_function(objective)


        # self.create_variables()

    def choose_objective_function(self, objective):
        if objective == "min":
            return self.find_minimum_node
        elif objective == "max":
            return self.find_maximum_node
        else:
            raise Exception("Objective function not defined")

    def create_variables(self):
        self.variables = []
        for i in range(self.n_variables):
            variable = Variable()
            variable.set_range(self.variable_ranges[i], "binary")
            self.variables.append(variable)

    
    def obtain_current_value(self):
        current_value = 0
        for i in range(self.n_variables):
            if not self.variables[i].is_variable_set():
                raise Exception("Variable " + str(i) + " is not set")
            
            current_value = self.math_operation(self.function_operations[i], current_value,
                                                self.weights[i] * self.variables[i].value)
        return current_value
        
    def math_operation(self, operation, value_one, value_two):
        if operation == "+":
            return value_one + value_two
        elif operation == "-":
            return value_one - value_two
        else:
            return None
        
    def anti_dijkstra(self, root_node):
        next_node = DijkstraNode(root_node, 0)
        self.unvisited_nodes.append(next_node)
        while next_node.node.id_node != 't':
            self.update_lists(next_node)
            next_node = self.objective_function()

        print("Mejor camino", next_node.weight)
        self.print_inverse_route(next_node)




    def print_inverse_route(self, terminal_node):
        current_node = terminal_node
        route = deque()
        while current_node.parent != None:
            route.appendleft(current_node.node.id_node)
            current_node = current_node.parent
        print(" -> ".join(route))


    def find_maximum_node(self):
        next_node = self.unvisited_nodes[0]
        for node in self.unvisited_nodes:
            if node.weight > next_node.weight:
                next_node = node
        return next_node
    
    def find_minimum_node(self):
        next_node = self.unvisited_nodes[0]
        for node in self.unvisited_nodes:
            if node.weight < next_node.weight:
                next_node = node
        return next_node
    
    def update_lists(self, next_node):
        self.visited_nodes.append(next_node)
        self.unvisited_nodes.remove(next_node)
        self.update_unvisited_nodes(next_node)

    def visited_nodes_or(self):
        visited_nodes = []
        for node in self.visited_nodes:
            visited_nodes.append(node.node)
        return visited_nodes


    def update_unvisited_nodes(self, next_node):
        for arc in next_node.node.out_arcs:
            if arc.in_node not in self.visited_nodes_or():

                self.unvisited_nodes.append(DijkstraNode(arc.in_node, next_node.weight + arc.variable_value, next_node))
        


class Variable:

    def __init__(self):
        self.value = None
        self.range = None

    def set_value(self, value):
        self.value = value

    def set_range(self, range, type):
        self.range = Range(range, type)

    def is_value_in_range(self, value):
        return self.range.in_range(value)
    
    def is_variable_set(self):
        return self.value != None
    
class DijkstraNode:

    def __init__(self, node, weight, parent=None):
        self.node = node
        self.weight = weight
        self.parent = parent

class Range:

    def __init__(self, range, type):
        self.range = range
        self.define_type(type)

    def define_type(self, type):
        if type == "between_two_values":
            self.in_range = self.between_two_values
        elif type == "binary":
            self.in_range = self.binary
        elif type == "in_list":
            self.in_range = self.in_list

    def between_two_values(self, value):
        return value >= self.range[0] and value <= self.range[1]
    
    def binary(self, value):
        return value == 0 or value == 1
    
    def in_list(self, value):
        return value in self.range
