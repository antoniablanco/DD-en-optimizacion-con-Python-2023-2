from Class.Node import Node
from Class.Arc import Arc
from Class.Graph import Graph

import copy


class ReduceConstructor():

    def __init__(self, graph):
        self.graph = copy.deepcopy(graph)
        self.layerWorking = self.graph.actual_layer 
    
    def print_layer(self):
        print("")
        for layer in self.graph.structure:
            print("------------------------------------------------------")
            for node in layer:
                in_arcs_str = ", ".join(str(arc) for arc in node.in_arcs) 
                print(str(node) + "(" + in_arcs_str + ")", end=" ")
            print("")
    
    def get_reduce_decision_diagram(self):
        for layer in reversed(self.graph.structure[:-1]): 
            self.print_layer() #Sacar
            self.layerWorking -= 1 
            self.reviewing_layer(layer)
        self.update_node_names()
        self.eliminate_edge_from_nodes_that_node_exist(self.graph.structure[-1][0])
        self.print_layer() #Sacar
                
        return self.graph
    
    def reviewing_layer(self, layer):

        for i, node_one in enumerate(layer):
            nodes = layer[i+1:]  # Copia de la lista original de nodos para evitar problemas con la iteración

            while len(nodes) > 0:
                node_two = nodes.pop(0)
                if self.checking_if_two_nodes_should_merge(node_one, node_two):
                    self.merge_nodes(node_one, node_two)
    
    def checking_if_two_nodes_should_merge(self, node_one, node_two):
        NodesOfPathNodeOne = self.get_node_of_every_type_of_path(node_one)
        NodesOfPathNodeTwo = self.get_node_of_every_type_of_path(node_two)
        if NodesOfPathNodeOne == NodesOfPathNodeTwo:
            return True

    def get_node_of_every_type_of_path(self, node):
        NodesOfPath = {}
        for arc in node.out_arcs:
            NodesOfPath[arc.in_node] = arc.variable_value
        return NodesOfPath

    def merge_nodes(self, node_one, node_two):
        nodes = list(self.get_order_of_changin_nodes(node_one, node_two))
        changin_nodes_ordered = [nodes[0], nodes[1]]
        
        self.redirect_in_arcs(changin_nodes_ordered)
        self.redirect_out_arcs(changin_nodes_ordered)
        self.delete_node(changin_nodes_ordered)
    
    def get_order_of_changin_nodes(self, node_one, node_two):
        current_layer = self.graph.structure[self.layerWorking]
        if node_one in current_layer and node_two in current_layer:
            if current_layer.index(node_one) > current_layer.index(node_two):
                return (node_one, node_two)  
            else:
                return (node_two, node_one)
        else:
            print("Error: No se encuentran los nodos en la capa actual")
    
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
    
    def update_node_names(self):
        valor_actual = 1

        for layer in self.graph.structure[1:]:
            for node in layer:
                if node.id_node!='t':
                    node.id_node = str(valor_actual)
                    valor_actual += 1
    
    def eliminate_edge_from_nodes_that_node_exist(self, node):
        for arc in node.in_arcs:
            if arc.out_node not in self.graph.nodes:
                node.in_arcs.remove(arc)
    