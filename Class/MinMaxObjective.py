from collections import deque

class MinMaxFunction:

    def __init__(self, weights, objective):
        self.weights = weights

        self.visited_nodes = []
        self.unvisited_nodes = []
        self.objective = objective
        self.choose_transform_weights()


        # self.create_variables()

    def choose_transform_weights(self):
        if self.objective == "max":
            self.weights = [-weight for weight in self.weights]

    def assign_graph(self, graph):
        self.assign_transition_values(graph)
        self.assing_terminal_node_id(graph.structure[-1][0])
        
    def assign_transition_values(self, graph):
        for level in range(0, len(graph.structure) - 1):
            for node in graph.structure[level]:
                for arc in node.out_arcs:
                    self.assing_value_to_arc(arc, level)

    def assing_terminal_node_id(self, terminal_node):
        self.terminal_node = terminal_node


    def assing_value_to_arc(self, arc, level):
        arc.transicion_value = self.weights[level] * arc.variable_value
        
    def anti_dijkstra(self, root_node):
        next_node = root_node
        next_node.update_weight(0)
        self.unvisited_nodes.append(next_node)
        while next_node.id_node != self.terminal_node.id_node:
            self.update_lists(next_node)
            next_node = self.find_minimum_node()

        self.print_inverse_route(next_node)

    def dfs_start(self, root_node):
        weight, route = self.dfs_for_max_distance(root_node, 0)

        self.print_best_weight_route(weight, route)

    def print_best_weight_route(self, weight, route):
        # print("Best Route:"," -> ".join(route))

        print("Best Route:"," -> ".join(map(str, route)))
        if self.objective == "max":
            print("Weight: " + str(-weight))
        else:
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
            if self.objective == "max":
                route.appendleft((current_node.id_node, -current_node.weight))
            else:
                route.appendleft((current_node.id_node, current_node.weight))
            current_node = current_node.parent
        
        
        self.print_best_weight_route(terminal_node.weight, route)
    
    def find_minimum_node(self):
        next_node = self.unvisited_nodes[0]
        best_value = float('inf')
        for node in self.unvisited_nodes:
            for arc in node.out_arcs:
                if arc.transicion_value < best_value:
                    best_value = arc.transicion_value
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
                if node.weight > next_node.weight + arc.transicion_value:
                    node.update_weight(next_node.weight + arc.transicion_value)
                    node.update_parent(next_node)
                    self.unvisited_nodes.append(node)
                    # self.visited_nodes.remove(node)