from Class.Node import Node
from Class.Arc import Arc
from Class.Graph import Graph


node_root = Node(0, initial_state)

graph = Graph(node_root)

node_1 = Node(1, [0])
node_2 = Node(2, [3])
node_3 = Node(3, [0])
node_4 = Node(4, [3])
node_5 = Node(5, [6])
node_6 = Node(6, [0])
node_7 = Node(7, [4])
node_8 = Node(8, [3])
node_9 = Node(9, [6])
node_10 = Node(3, [])

self.graph.new_layer()

arc = Arc(existed_node, node_created, variable_value, self._variables[variable_id])
node_created = Node(str(self._node_number), node_state)
self.graph.add_node(node_created)