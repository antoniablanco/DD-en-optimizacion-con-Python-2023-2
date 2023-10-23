from Class.Node import Node
from Class.Arc import Arc
from Class.Graph import Graph

class Constructor():

    def __init__(self, problem):
        self.node_number = 1
        self.graph = None

        self.problem = problem
        self.initial_state = problem.initial_state
        self.variables = problem.ordered_variables
        self.variables_domain = problem.variables_domain

        self.initialize_graph()
    
    def print_layer(self):
        '''
        print("")
        for layer in self.graph.structure:
            print("------------------------------------------------------")
            for node in layer:
                in_arcs_str = ", ".join(str(arc) for arc in node.in_arcs) 
                print(str(node) + "(" + in_arcs_str + ")", end=" ")
            print("")
        '''
        
    def initialize_graph(self):
        node_root = Node(0, self.initial_state)
        self.graph = Graph(node_root)
    
    def get_decision_diagram(self):
        for variable_id in range(len(self.variables)):
            self.create_new_layer(variable_id)
        
        self.merge_terminal_node()
        self.print_layer() 

        return self.graph
    
    def create_new_layer(self, variable_id):
        self.graph.new_layer()
        self.create_new_nodes_in_the_new_layer(variable_id)
        self.merge_nodes_with_same_state()
        self.print_layer()

    def create_new_nodes_in_the_new_layer(self, variable_id):
        for existed_node in self.graph.structure[-2][:]:
            for variable_value in self.variables_domain[self.variables[variable_id]]:
                self.create_the_new_node(variable_value, existed_node, variable_id)
    
    def create_the_new_node(self, variable_value, existed_node, variable_id):
        node_state, flag = self.problem.transition_function(existed_node.state, self.variables[variable_id], variable_value)
        if flag:
            node_created = Node(str(self.node_number), node_state)
            self.node_number += 1    
            self.create_arc_for_the_new_node(existed_node, node_created, variable_value, variable_id)
            self.graph.add_node(node_created)
 
    def create_arc_for_the_new_node(self, existed_node, node_created, variable_value, variable_id):  
        arc = Arc(existed_node, node_created, variable_value, self.variables[variable_id])
        existed_node.add_out_arc(arc)
        node_created.add_in_arc(arc)
    
    def merge_nodes_with_same_state(self):
        last_layer = self.graph.structure[-1][:]
        for i, node_one in enumerate(last_layer):
            for j, node_two in enumerate(last_layer):
                self.search_node_to_merge(node_one, node_two, i, j)
    
    def search_node_to_merge(self, node_one, node_two, i, j):
        if i < j and node_one.id_node != node_two.id_node and self.checking_if_two_nodes_have_same_state(node_one, node_two):
            self.merge_nodes(node_one, node_two)

    def checking_if_two_nodes_have_same_state(self, node_one, node_two):
        return self.problem.equals(node_one.state, node_two.state)

    def merge_nodes(self, node_one, node_two):
        nodes = list(self.get_order_of_changin_nodes(node_one, node_two))
        changin_nodes_ordered = [nodes[0], nodes[1]]
        
        self.redirect_in_arcs(changin_nodes_ordered)
        self.redirect_out_arcs(changin_nodes_ordered)
        self.delete_node(changin_nodes_ordered)
        self.update_self_informacion(changin_nodes_ordered)
    
    def get_order_of_changin_nodes(self, node_one, node_two):
        current_layer = self.graph.structure[self.graph.actual_layer]
        if node_one in current_layer and node_two in current_layer:
            if current_layer.index(node_one) > current_layer.index(node_two):
                return (node_one, node_two)  
            else:
                return (node_two, node_one)

    def redirect_in_arcs(self, changin_nodes_ordered):
        for arc in changin_nodes_ordered[0].in_arcs:
            arc.in_node = changin_nodes_ordered[1]
            if arc not in changin_nodes_ordered[1].in_arcs:
                changin_nodes_ordered[1].add_in_arc(arc)

    def redirect_out_arcs(self, changin_nodes_ordered):
        for arc in changin_nodes_ordered[0].out_arcs:
            arc.out_node = changin_nodes_ordered[1]
            if arc not in changin_nodes_ordered[1].out_arcs:
                changin_nodes_ordered[1].add_out_arc(arc)
    
    def delete_node(self, changin_nodes_ordered):
        self.graph.remove_node(changin_nodes_ordered[0])
        del changin_nodes_ordered[0]
    
    def update_self_informacion(self, changin_nodes_ordered):
        self.node_number -= 1
        index_node, index_layer = self.graph.get_index_node(changin_nodes_ordered[0])
        self.update_node_names(index_node, index_layer)
    
    def update_node_names(self, index_node, index_layer):
        valor_actual = int(self.graph.structure[index_layer-1][-1].id_node)
        for i, node in enumerate(self.graph.structure[index_layer]):
            if i == index_node and node.id_node!='t':
                valor_actual = int(node.id_node) + 1
            elif i > index_node and node.id_node!='t':
                node.id_node = str(valor_actual)
                valor_actual += 1

    def merge_terminal_node(self):
        last_layer = self.graph.structure[-1][:]
        final_node = Node(len(self.graph.nodes), [])
        self.graph.add_final_node(final_node)

        for node_one in last_layer:
            self.merge_nodes(node_one, final_node)
        final_node.id_node = len(self.graph.nodes)

