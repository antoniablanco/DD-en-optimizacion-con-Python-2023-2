from collections import deque


class LinearObjective:

    def __init__(self, weights, objective):
        self._weights = weights

        self._visited_nodes = []
        self._unvisited_nodes = []
        self._objective = objective
        self._choose_transform_weights()

    def _choose_transform_weights(self):
        if self._objective == "max":
            self._weights = [-weight for weight in self._weights]

    def assign_graph(self, graph):
        # self.assign_transition_values(graph)
        self._graph = graph
        self._assing_terminal_node_id(graph.structure[-1][0])
        
    # def assign_transition_values(self, graph):
    #     for level in range(0, len(graph.structure) - 1):
    #         for node in graph.structure[level]:
    #             for arc in node.out_arcs:
    #                 self.assing_value_to_arc(arc, level)

    def _assing_terminal_node_id(self, terminal_node):
        self._terminal_node = terminal_node

    def _get_arc_transition_value(self, arc, level):
        arc.transition_value = self._weights[level] * arc.variable_value
        return self._weights[level] * arc.variable_value
        
    def dijkstra(self, root_node):
        next_node = root_node
        next_node.update_weight(0)
        self._unvisited_nodes.append(next_node)
        while next_node.id_node != self._terminal_node.id_node:
            self._update_lists(next_node)
            next_node = self._find_minimum_node()

        self._save_results(next_node)

    def _transform_best_weight(self, terminal_node):
        weight = terminal_node.weight
        if self._objective == "max":
            return -weight
        else:
            return weight
        
    def _save_results(self, terminal_node):
       
        self._best_route = self._get_route_of_node(terminal_node)
        weight = terminal_node.weight
        if self._objective == "max":
            self._best_weight =  -weight
        else:
            self._best_weight =  weight

    def _get_route_of_node(self, node):
        current_node = node
        route = deque()
        while current_node != None:
            if self._objective == "max":
                route.appendleft((current_node.id_node, -current_node.weight))
            else:
                route.appendleft((current_node.id_node, current_node.weight))
            current_node = current_node.parent
        route = " -> ".join(map(str, route))
        return route
    
    def get_best_route(self):
        return self._best_route
    
    def get_best_weight(self):
        return self._best_weight

    def _print_best_weight_route(self, weight, route):
        print("Best Route:", self._best_route)
        print("Best Weight:", self._best_weight)
    
    def _find_minimum_node(self):
        next_node = self._unvisited_nodes[0]
        best_value = float('inf')
        for node in self._unvisited_nodes:
            node_level = self._get_node_level(node)
            for arc in node.out_arcs:
                transition_value = self._get_arc_transition_value(arc, node_level)
                if transition_value < best_value:
                    best_value = transition_value
                    next_node = node
        return next_node
    
    def _update_lists(self, next_node):
        self._visited_nodes.append(next_node)
        self._unvisited_nodes.remove(next_node)
        self._update_unvisited_nodes(next_node)

    def _update_unvisited_nodes(self, next_node):
        node_level = self._get_node_level(next_node)
        for arc in next_node.out_arcs:
            if arc.in_node not in self._visited_nodes and arc.in_node not in self._unvisited_nodes:
                node = arc.in_node
                transition_value = self._get_arc_transition_value(arc, node_level)
                node.update_weight(next_node.weight + transition_value)
                node.update_parent(next_node)
                self._unvisited_nodes.append(node)

            else:
                node = arc.in_node
                transition_value = self._get_arc_transition_value(arc, node_level)
                if node.weight > next_node.weight + transition_value:
                    node.update_weight(next_node.weight + transition_value)
                    node.update_parent(next_node)
                    self._unvisited_nodes.append(node)
                    # self.visited_nodes.remove(node)

    def _get_node_level(self, node):
        for level in range(0, len(self._graph.structure)):
            if node in self._graph.structure[level]:
                return level

    