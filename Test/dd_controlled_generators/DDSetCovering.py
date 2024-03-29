import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)

from Class.DDStructure.Node import Node
from Class.DDStructure.Arc import Arc
from Class.DDStructure.Graph import Graph

node_0 = Node('0', [1,2,3])
graph = Graph(node_0)


# Capa x_1
graph.new_layer()
node_1 = Node('1', [1, 2, 3])
arc_0_1 = Arc(node_0, node_1, 0, 'x_1')
node_0.add_out_arc(arc_0_1)
node_1.add_in_arc(arc_0_1)
graph.add_node(node_1)

node_2 = Node('2', [3])
arc_0_2 = Arc(node_0, node_2, 1, 'x_1')
node_0.add_out_arc(arc_0_2)
node_2.add_in_arc(arc_0_2)
graph.add_node(node_2)

# Capa x_2
graph.new_layer()
node_3 = Node('3', [1, 2, 3])
arc_1_3 = Arc(node_1, node_3, 0, 'x_2')
node_1.add_out_arc(arc_1_3)
node_3.add_in_arc(arc_1_3)
graph.add_node(node_3)

node_4 = Node('4', [2])
arc_1_4 = Arc(node_1, node_4, 1, 'x_2')
node_1.add_out_arc(arc_1_4)
node_4.add_in_arc(arc_1_4)
graph.add_node(node_4)

node_5 = Node('5', [3])
arc_2_5 = Arc(node_2, node_5, 0, 'x_2')
node_2.add_out_arc(arc_2_5)
node_5.add_in_arc(arc_2_5)
graph.add_node(node_5)

node_6 = Node('6', [])
arc_2_6 = Arc(node_2, node_6, 1, 'x_2')
node_2.add_out_arc(arc_2_6)
node_6.add_in_arc(arc_2_6)
graph.add_node(node_6)

# Capa x_3
graph.new_layer()
node_7 = Node('7', [2, 3])
arc_3_7 = Arc(node_3, node_7, 1, 'x_3')
node_3.add_out_arc(arc_3_7)
node_7.add_in_arc(arc_3_7)
graph.add_node(node_7)

node_8 = Node('8', [2])
arc_4_8_op1 = Arc(node_4, node_8, 0, 'x_3')
arc_4_8_op2 = Arc(node_4, node_8, 1, 'x_3')
node_4.add_out_arc(arc_4_8_op1)
node_4.add_out_arc(arc_4_8_op2)
node_8.add_in_arc(arc_4_8_op1)
node_8.add_in_arc(arc_4_8_op2)
graph.add_node(node_8)

node_9 = Node('9', [3])
arc_5_9_op1 = Arc(node_5, node_9, 0, 'x_3')
arc_5_9_op2 = Arc(node_5, node_9, 1, 'x_3')
node_5.add_out_arc(arc_5_9_op1)
node_5.add_out_arc(arc_5_9_op2)
node_9.add_in_arc(arc_5_9_op1)
node_9.add_in_arc(arc_5_9_op2)
graph.add_node(node_9)

node_10 = Node('10', [])
arc_6_10_op1 = Arc(node_6, node_10, 0, 'x_3')
arc_6_10_op2 = Arc(node_6, node_10, 1, 'x_3')
node_6.add_out_arc(arc_6_10_op1)
node_6.add_out_arc(arc_6_10_op2)
node_10.add_in_arc(arc_6_10_op1)
node_10.add_in_arc(arc_6_10_op2)
graph.add_node(node_10)

# Capa x_4
graph.new_layer()

node_11 = Node('11', [2, 3])
arc_7_11 = Arc(node_7, node_11, 0, 'x_4')
node_7.add_out_arc(arc_7_11)
node_11.add_in_arc(arc_7_11)
graph.add_node(node_11)

node_12 = Node('12', [])
arc_7_12 = Arc(node_7, node_12, 1, 'x_4')
arc_8_12 = Arc(node_8, node_12, 1, 'x_4')
arc_9_12 = Arc(node_9, node_12, 1, 'x_4')
arc_10_12_op1 = Arc(node_10, node_12, 0, 'x_4')
arc_10_12_op2 = Arc(node_10, node_12, 1, 'x_4')
node_7.add_out_arc(arc_7_12)
node_8.add_out_arc(arc_8_12)
node_9.add_out_arc(arc_9_12)
node_10.add_out_arc(arc_10_12_op1)
node_10.add_out_arc(arc_10_12_op2)
node_12.add_in_arc(arc_7_12)
node_12.add_in_arc(arc_8_12)
node_12.add_in_arc(arc_9_12)
node_12.add_in_arc(arc_10_12_op1)
node_12.add_in_arc(arc_10_12_op2)
graph.add_node(node_12)

node_13 = Node('13', [2])
arc_8_13 = Arc(node_8, node_13, 0, 'x_4')
node_8.add_out_arc(arc_8_13)
node_13.add_in_arc(arc_8_13)
graph.add_node(node_13)

node_14 = Node('14', [3])
arc_9_14 = Arc(node_9, node_14, 0, 'x_4')
node_9.add_out_arc(arc_9_14)
node_14.add_in_arc(arc_9_14)
graph.add_node(node_14)

# Capa x_5
graph.new_layer()
node_15 = Node('15', [3])
arc_11_15 = Arc(node_11, node_15, 1, 'x_5')
arc_14_15_op1 = Arc(node_14, node_15, 1, 'x_5')
arc_14_15_op2 = Arc(node_14, node_15, 0, 'x_5')
node_11.add_out_arc(arc_11_15)
node_14.add_out_arc(arc_14_15_op1)
node_14.add_out_arc(arc_14_15_op2)
node_15.add_in_arc(arc_11_15)
node_15.add_in_arc(arc_14_15_op1)
node_15.add_in_arc(arc_14_15_op2)
graph.add_node(node_15)

node_16 = Node('16', [])
arc_12_16_op1 = Arc(node_12, node_16, 0, 'x_5')
arc_12_16_op2 = Arc(node_12, node_16, 1, 'x_5')
arc_13_16 = Arc(node_13, node_16, 1, 'x_5')
node_12.add_out_arc(arc_12_16_op1)
node_12.add_out_arc(arc_12_16_op2)
node_13.add_out_arc(arc_13_16)
node_16.add_in_arc(arc_12_16_op1)
node_16.add_in_arc(arc_12_16_op2)
node_16.add_in_arc(arc_13_16)
graph.add_node(node_16)

# Capa x_6
graph.new_layer()
node_17 = Node('17', [])
arc_15_17 = Arc(node_15, node_17, 1, 'x_6')
arc_16_17_op1 = Arc(node_16, node_17, 0, 'x_6')
arc_16_17_op2 = Arc(node_16, node_17, 1, 'x_6')
node_15.add_out_arc(arc_15_17)
node_16.add_out_arc(arc_16_17_op1)
node_16.add_out_arc(arc_16_17_op2)
node_17.add_in_arc(arc_15_17)
node_17.add_in_arc(arc_16_17_op1)
node_17.add_in_arc(arc_16_17_op2)
graph.add_node(node_17)