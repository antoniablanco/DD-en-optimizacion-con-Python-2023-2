from Class.Node import Node
from Class.Arc import Arc
from Class.Graph import Graph


class Constructor():

    def __init__(self, problem):
        self._node_number = 1
        self.graph = None

        self._problem = problem
        self._variables = problem.ordered_variables
        self._variables_domain = problem.variables_domain

        self._initialize_graph(problem.initial_state)
        
    def _initialize_graph(self, initial_state):
        node_root = Node(0, initial_state)
        self.graph = Graph(node_root)
    
    def get_decision_diagram(self, should_visualize):
        for variable_id in range(len(self._variables)):
            self._create_new_layer(variable_id)
            self._print_graph(should_visualize)
        
        self._print_graph(should_visualize)

        return self.graph
    
    def _create_new_layer(self, variable_id):
        self.graph.new_layer()
        self._create_new_nodes_in_the_new_layer(variable_id)

    def _create_new_nodes_in_the_new_layer(self, variable_id):
        for existed_node in self.graph.structure[-2][:]:
            for variable_value in self._variables_domain[self._variables[variable_id]]:
                self._check_if_new_node_should_be_created(variable_value, existed_node, variable_id)
    
    def _check_if_new_node_should_be_created(self, variable_value, existed_node, variable_id):
        node_state, isFeasible = self._problem.transition_function(existed_node.state, self._variables[variable_id], variable_value)
        if isFeasible:
            if self._there_is_node_in_last_layer(variable_id):
                self._create_arcs_for_the_terminal_node(existed_node,variable_value, variable_id)
            else:
                self._create_rest_of_arcs(existed_node, variable_value, variable_id, node_state)
    
    def _there_is_node_in_last_layer(self, variable_id):
        return self._variables[-1] == self._variables[variable_id] and self.graph.structure[-1] != []
    
    def _create_arcs_for_the_terminal_node(self, existed_node, variable_value, variable_id):
        same_state_node = self.graph.structure[-1][-1]
        self._create_arc_for_the_new_node(existed_node, same_state_node, variable_value, variable_id)
    
    def _create_rest_of_arcs(self, existed_node, variable_value, variable_id, node_state):
        nodo_existe, same_state_node = self._exist_node_with_same_state(node_state)
        if nodo_existe:
            self._create_arc_for_the_new_node(existed_node, same_state_node, variable_value, variable_id)
        else:
            node_created = Node(str(self._node_number), node_state)
            self._node_number += 1    
            self._create_arc_for_the_new_node(existed_node, node_created, variable_value, variable_id)
            self.graph.add_node(node_created)

    def _exist_node_with_same_state(self, node_state):
        for node in self.graph.structure[-1]:
            if self._problem.equals(node.state, node_state):
                return True, node
        return False, None

    def _create_arc_for_the_new_node(self, existed_node, node_created, variable_value, variable_id):  
        arc = Arc(existed_node, node_created, variable_value, self._variables[variable_id])
        existed_node.add_out_arc(arc)
        node_created.add_in_arc(arc)
    
    '''
    def _merge_nodes_with_same_state(self):
        last_layer = self.graph.structure[-1][:]
        for i, node_one in enumerate(last_layer):
            for j, node_two in enumerate(last_layer):
                self._search_node_to_merge(node_one, node_two, i, j)
    
    def _search_node_to_merge(self, node_one, node_two, i, j):
        if i < j and node_one.id_node != node_two.id_node and self._checking_if_two_nodes_have_same_state(node_one, node_two):
            self._merge_nodes(node_one, node_two)

    def _checking_if_two_nodes_have_same_state(self, node_one, node_two):
        return self._problem.equals(node_one.state, node_two.state)

    def _merge_nodes(self, node_one, node_two):
        nodes = list(self._get_order_of_changin_nodes(node_one, node_two))
        changin_nodes_ordered = [nodes[0], nodes[1]]
        
        self._redirect_in_arcs(changin_nodes_ordered)
        self._redirect_out_arcs(changin_nodes_ordered)
        self._delete_node(changin_nodes_ordered)
        self._update_self_informacion(changin_nodes_ordered)
    
    def _get_order_of_changin_nodes(self, node_one, node_two):
        current_layer = self.graph.structure[self.graph.actual_layer]
        if node_one in current_layer and node_two in current_layer:
            if current_layer.index(node_one) > current_layer.index(node_two):
                return (node_one, node_two)  
            else:
                return (node_two, node_one)

    def _redirect_in_arcs(self, changin_nodes_ordered):
        for arc in changin_nodes_ordered[0].in_arcs:
            arc.in_node = changin_nodes_ordered[1]
            if arc not in changin_nodes_ordered[1].in_arcs:
                changin_nodes_ordered[1].add_in_arc(arc)

    def _redirect_out_arcs(self, changin_nodes_ordered):
        for arc in changin_nodes_ordered[0].out_arcs:
            arc.out_node = changin_nodes_ordered[1]
            if arc not in changin_nodes_ordered[1].out_arcs:
                changin_nodes_ordered[1].add_out_arc(arc)
    
    def _delete_node(self, changin_nodes_ordered):
        self.graph.remove_node(changin_nodes_ordered[0])
        del changin_nodes_ordered[0]
    
    def _update_self_informacion(self, changin_nodes_ordered):
        self._node_number -= 1
        index_node, index_layer = self.graph.get_index_node(changin_nodes_ordered[0])
        self._update_node_names(index_node, index_layer)
    
    def _update_node_names(self, index_node, index_layer):
        valor_actual = int(self.graph.structure[index_layer-1][-1].id_node)
        for i, node in enumerate(self.graph.structure[index_layer]):
            if i == index_node and node.id_node!='t':
                valor_actual = int(node.id_node) + 1
            elif i > index_node and node.id_node!='t':
                node.id_node = str(valor_actual)
                valor_actual += 1

    def _merge_terminal_node(self):
        last_layer = self.graph.structure[-1][:]
        final_node = Node(len(self.graph.nodes), [])
        self.graph.add_final_node(final_node)

        for node_one in last_layer:
            self._merge_nodes(node_one, final_node)
        final_node.id_node = len(self.graph.nodes)-1
    '''

    def _print_graph(self, should_visualize):
        if should_visualize:
            self._print()

    def _print(self):
        print("")
        for layer in self.graph.structure:
            print("------------------------------------------------------")
            for node in layer:
                in_arcs_str = ", ".join(str(arc) for arc in node.in_arcs) 
                print(str(node) + "(" + in_arcs_str + ")", end=" ")
            print("")
    
