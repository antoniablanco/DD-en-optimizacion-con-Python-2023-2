from Class.Node import Node
from Class.Arc import Arc
from Class.Graph import Graph

# Create nodes and graph
node_0 = Node('0', [1, 2, 3, 4, 5])
graph = Graph(node_0)

# Layer 1
graph.new_layer()
node_1 = Node('1', [2, 3, 4, 5])
arc_0_1 = Arc(node_0, node_1, 0, 'arc_0_1')
node_0.add_out_arc(arc_0_1)
node_1.add_in_arc(arc_0_1)
graph.add_node(node_1)

node_2 = Node('2', [4, 5])
arc_0_2 = Arc(node_0, node_2, 1, 'arc_0_2')
node_0.add_out_arc(arc_0_2)
node_2.add_in_arc(arc_0_2)
graph.add_node(node_2)

# Layer 2
graph.new_layer()
node_3 = Node('3', [3, 4, 5])
arc_1_3 = Arc(node_1, node_3, 0, 'arc_1_3')
node_1.add_out_arc(arc_1_3)
node_3.add_in_arc(arc_1_3)
graph.add_node(node_3)

node_4 = Node('4', [5])
arc_1_4 = Arc(node_1, node_4, 0, 'arc_1_4')
node_1.add_out_arc(arc_1_4)
node_4.add_in_arc(arc_1_4)

node_5 = Node('5', [4, 5])
arc_2_5 = Arc(node_2, node_5, 0, 'arc_2_5')
node_2.add_out_arc(arc_2_5)
node_5.add_in_arc(arc_2_5)
graph.add_node(node_5)

# Layer 3
graph.new_layer()
node_6 = Node('6', [4, 5])
arc_3_6 = Arc(node_3, node_6, 0, 'arc_3_6')
node_3.add_out_arc(arc_3_6)
node_6.add_in_arc(arc_3_6)

arc_5_6 = Arc(node_5, node_6, 0, 'arc_5_6')
node_5.add_out_arc(arc_5_6)
node_6.add_in_arc(arc_5_6)

node_7 = Node('7', [5])
arc_3_7 = Arc(node_3, node_7, 0, 'arc_3_7')
node_3.add_out_arc(arc_3_7)
node_7.add_in_arc(arc_3_7)

arc_4_7 = Arc(node_4, node_7, 0, 'arc_4_7')
node_4.add_out_arc(arc_4_7)
node_7.add_in_arc(arc_4_7)
graph.add_node(node_7)

# Layer 4
graph.new_layer()
node_8 = Node('8', [5])
arc_6_8 = Arc(node_6, node_8, 0, 'arc_6_8')
node_6.add_out_arc(arc_6_8)
node_8.add_in_arc(arc_6_8)

arc_7_8 = Arc(node_7, node_8, 0, 'arc_7_8')
node_7.add_out_arc(arc_7_8)
node_8.add_in_arc(arc_7_8)

node_9 = Node('9', [])
arc_6_9 = Arc(node_6, node_9, 0, 'arc_6_9')
node_6.add_out_arc(arc_6_9)
node_9.add_in_arc(arc_6_9)

# Layer 5
graph.new_layer()
node_10 = Node('10', [])
arc_8_10_op1 = Arc(node_8, node_10, 0, 'arc_8_10')
node_8.add_out_arc(arc_8_10_op1)
node_10.add_in_arc(arc_8_10_op1)

arc_8_10_op2 = Arc(node_8, node_10, 1, 'arc_8_10')
node_8.add_out_arc(arc_8_10_op2)
node_10.add_in_arc(arc_8_10_op2)

arc_9_10 = Arc(node_9, node_10, 0, 'arc_9_10')
node_9.add_out_arc(arc_9_10)
node_10.add_in_arc(arc_9_10)
