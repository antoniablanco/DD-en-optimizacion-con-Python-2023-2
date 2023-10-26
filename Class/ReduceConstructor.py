from Class.Node import Node
from Class.Arc import Arc
from Class.Graph import Graph

import copy


class ReduceConstructor():

    def __init__(self, graph):
        self._graph = copy.deepcopy(graph)
        self._layerWorking = self._graph.actual_layer
    
    def get_reduce_decision_diagram(self, should_visualize):
        for layer in reversed(self._graph.structure[:-1]):
            self._print_graph(should_visualize)
            self._layerWorking -= 1 
            self._reviewing_layer(layer)

        self._final_layer_set_up()
        self._print_graph(should_visualize)
                
        return self._graph
    
    def _print_graph(self, should_visualize):
        if should_visualize:
            self._print()

    def _print(self):
        print("")
        for layer in self._graph.structure:
            print("------------------------------------------------------")
            for node in layer:
                in_arcs_str = ", ".join(str(arc) for arc in node.in_arcs) 
                print(str(node) + "(" + in_arcs_str + ")", end=" ")
            print("")
    
    def _reviewing_layer(self, layer):

        for i, node_one in enumerate(layer):
            nodes = layer[i+1:]  

            while len(nodes) > 0:
                node_two = nodes.pop(0)
                if self._checking_if_two_nodes_should_merge(node_one, node_two):
                    self._merge_nodes(node_one, node_two)
    
    def _checking_if_two_nodes_should_merge(self, node_one, node_two):
        NodesOfPathNodeOne = self._get_node_of_every_type_of_path(node_one)
        NodesOfPathNodeTwo = self._get_node_of_every_type_of_path(node_two)
        if NodesOfPathNodeOne == NodesOfPathNodeTwo:
            return True

    def _get_node_of_every_type_of_path(self, node):
        NodesOfPath = {}
        for arc in node.out_arcs:
            NodesOfPath[arc.in_node] = arc.variable_value
        return NodesOfPath

    def _merge_nodes(self, node_one, node_two):
        nodes = list(self._get_order_of_changin_nodes(node_one, node_two))
        changin_nodes_ordered = [nodes[0], nodes[1]]
        
        self._redirect_in_arcs(changin_nodes_ordered)
        self._redirect_out_arcs(changin_nodes_ordered)
        self._delete_node(changin_nodes_ordered)
    
    def _get_order_of_changin_nodes(self, node_one, node_two):
        current_layer = self._graph.structure[self._layerWorking]
        if node_one in current_layer and node_two in current_layer:
            if current_layer.index(node_one) > current_layer.index(node_two):
                return (node_one, node_two)  
            else:
                return (node_two, node_one)
        else:
            print("Error: No se encuentran los nodos en la capa actual")
    
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
        self._graph.remove_node(changin_nodes_ordered[0])
        del changin_nodes_ordered[0]
    
    def _final_layer_set_up(self):
        self._update_node_names()
        self._eliminate_edge_from_nodes_that_node_exist(self._graph.structure[-1][0])
        self._eliminate_duplicate_edge()

    def _update_node_names(self):
        valor_actual = 1

        for layer in self._graph.structure[1:]:
            for node in layer:
                if node.id_node!='t':
                    node.id_node = str(valor_actual)
                    valor_actual += 1
    
    def _eliminate_edge_from_nodes_that_node_exist(self, node):
        for arc in node.in_arcs:
            if arc.out_node not in self._graph.nodes:
                node.in_arcs.remove(arc)

    def _eliminate_duplicate_edge(self):
        for node in self._graph.nodes:
            unique_arcs = set()
            for i, arc1 in enumerate(node.in_arcs[:-1]):
                if arc1 in unique_arcs:
                    continue  
                for arc2 in node.in_arcs[i+1:]:
                    if arc1.variable_value == arc2.variable_value and arc1.out_node == arc2.out_node:
                        node.in_arcs.remove(arc2)
                        arc2.out_node.out_arcs.remove(arc2)
                    else:
                        unique_arcs.add(arc1)  
