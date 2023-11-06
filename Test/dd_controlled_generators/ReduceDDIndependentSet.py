from Class.Node import Node
from Class.Arc import Arc
from Class.Graph import Graph

# Create nodes
node_0 = Node('0', [0])
node_1 = Node('1', [0])
node_2 = Node('2', [0])
node_3 = Node('3', [0])
node_4 = Node('4', [0])
node_5 = Node('5', [0])
node_6 = Node('6', [0])
node_7 = Node('7', [0])
node_8 = Node('8', [0])
node_9 = Node('9', [0])
node_10 = Node('10', [0])
node_11 = Node('11', [0])

# Create arcs
arc_0_1 = Arc(node_0, node_1, 0, 'x_1')
arc_0_2 = Arc(node_0, node_2, 0, 'x_1')
arc_1_3 = Arc(node_1, node_3, 0, 'x_2')
arc_1_4 = Arc(node_1, node_4, 0, 'x_2')
arc_2_5 = Arc(node_2, node_5, 0, 'x_2')
arc_3_6 = Arc(node_3, node_6, 0, 'x_3')
arc_3_7 = Arc(node_3, node_7, 0, 'x_3')
arc_4_7 = Arc(node_4, node_7, 0, 'x_3')
arc_5_6 = Arc(node_5, node_6, 0, 'x_3')
arc_6_8 = Arc(node_6, node_8, 0, 'x_3')
arc_6_9 = Arc(node_6, node_9, 0, 'x_4')
arc_7_8 = Arc(node_7, node_8, 0, 'x_4')
arc_8_10_op1 = Arc(node_8, node_10, 0, 'x_4')
arc_8_10_op2 = Arc(node_8, node_10, 0, 'x_4')
arc_9_10 = Arc(node_9, node_10, 0, 'x_4')
arc_10_11 = Arc(node_10, node_11, 0, 'x_4')

# Create the graph and add nodes/arcs
graph = Graph(node_0)  # Assuming the graph starts with node_0
graph.new_layer()
graph.add_node(node_1)
graph.add_node(node_2)
graph.new_layer()
graph.add_node(node_3)
graph.add_node(node_4)
graph.new_layer()
graph.add_node(node_5)
graph.add_node(node_6)
graph.new_layer()
graph.add_node(node_7)
graph.add_node(node_8)
graph.add_node(node_9)
graph.new_layer()
graph.add_node(node_10)
graph.add_node(node_11)