from collections import deque

class MinMaxFunction:

    def __init__(self, variable_ranges, function_operations, weights, objective):
        self.variable_ranges = variable_ranges
        self.function_operations = function_operations
        self.weights = weights

        self.visited_nodes = []
        self.unvisited_nodes = []
        self.objective_function = self.choose_objective_function(objective)


        # self.create_variables()

    def choose_objective_function(self, objective):
        if objective == "min":
            return self.anti_dijkstra
        elif objective == "max":
            return self.dfs_start
        else:
            raise Exception("Objective function not defined")
        
    def assign_transition_values(self, graph):
        for level in range(0, len(graph.structure) - 1):
            for node in graph.structure[level]:
                for arc in node.out_arcs:
                    self.assing_value_to_arc(arc, level)


    def assing_value_to_arc(self, arc, level):
        arc.transicion_value = self.set_weight_value(level, self.weights[level]) * arc.variable_value

    def set_weight_value(self, level, value):
        if self.function_operations[level] == '-':
            return -value
    
        return value

    
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
        next_node = root_node
        next_node.update_weight(0)
        self.unvisited_nodes.append(next_node)
        while next_node.id_node != 't':
            self.update_lists(next_node)
            next_node = self.find_minimum_node()

        self.print_inverse_route(next_node)

    def dfs_start(self, root_node):
        weight, route = self.dfs_for_max_distance(root_node, 0)

        self.print_best_weight_route(weight, route)

    def print_best_weight_route(self, weight, route):
        # print("Best Route:"," -> ".join(route))

        print("Best Route:"," -> ".join(map(str, route)))
        print("Weight: " + str(weight))

    def dfs_for_max_distance(self, node, weight, route=[]):
        route.append((node.id_node, weight))
        if node.id_node == 't':
            return weight, route  # Return the weight and route list
            
        max_weight = 0
        best_route = route.copy()  # Create a new list with the updated route
        for arc in node.out_arcs:
            new_weight, new_route = self.dfs_for_max_distance(arc.in_node,
                                                            weight + arc.transicion_value,
                                                            route.copy())
            
            if new_weight > max_weight:
                max_weight = new_weight
                best_route = new_route

        return max_weight, best_route

        




    def print_inverse_route(self, terminal_node):
        current_node = terminal_node
        route = deque()
        while current_node != None:
            route.appendleft((current_node.id_node, current_node.weight))
            current_node = current_node.parent
        
        
        self.print_best_weight_route(terminal_node.weight, route)


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


    def update_unvisited_nodes(self, next_node):
        for arc in next_node.out_arcs:
            if arc.in_node not in self.visited_nodes and arc.in_node not in self.unvisited_nodes:
                node = arc.in_node
                node.update_weight(next_node.weight + arc.transicion_value)
                node.update_parent(next_node)
                self.unvisited_nodes.append(node)

            else:
                node = arc.in_node
                if self.get_node_weight(node) > next_node.weight + arc.transicion_value:
                    node.update_weight(next_node.weight + arc.transicion_value)
                    node.update_parent(next_node)
                    self.unvisited_nodes.append(node)
                    self.visited_nodes.remove(node, 1)

    def get_node_weight(self, node):
        return node.get_weight()

    def update_node_weight(self, node, weight):
        node.update_weight(weight)


    def compare_max_values(self, value_one, value_two):
        return value_one > value_two
    
    def compare_min_values(self, value_one, value_two):
        return value_one < value_two