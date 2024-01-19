import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)

from Class.DDStructure.Node import Node
from Class.DDStructure.Arc import Arc
from Class.DDStructure.Graph import Graph

node_0 = Node('0', [0])
graph = Graph(node_0)


graph.add_new_layer()
node_1 = Node('1', [0])
arc_0_1 = Arc(node_0, node_1, 0, 'x_1')
node_0.add_out_arc(arc_0_1)
node_1.add_in_arc(arc_0_1)

graph.add_node(node_1)
node_2 = Node('2', [3])
arc_0_2 = Arc(node_0, node_2, 1, 'x_1')
node_0.add_out_arc(arc_0_2)
node_2.add_in_arc(arc_0_2)
graph.add_node(node_2)


graph.add_new_layer()
node_3 = Node('3', [0])
arc_1_3 = Arc(node_1, node_3, 0, 'x_2')
node_1.add_out_arc(arc_1_3)
node_3.add_in_arc(arc_1_3)
graph.add_node(node_3)

node_4 = Node('4', [3])
arc_1_4 = Arc(node_1, node_4, 1, 'x_2')
node_1.add_out_arc(arc_1_4)
node_4.add_in_arc(arc_1_4)
arc_2_4 = Arc(node_2, node_4, 0, 'x_2')
node_2.add_out_arc(arc_2_4)
node_4.add_in_arc(arc_2_4)
graph.add_node(node_4)

graph.add_new_layer()
node_5 = Node('5', [0])
arc_3_5 = Arc(node_3, node_5, 0, 'x_3')
node_3.add_out_arc(arc_3_5)
node_5.add_in_arc(arc_3_5)
graph.add_node(node_5)

node_6 = Node('6', [4])
arc_3_6 = Arc(node_3, node_6, 1, 'x_3')
node_3.add_out_arc(arc_3_6)
node_6.add_in_arc(arc_3_6)
graph.add_node(node_6)

node_7 = Node('7', [3])
arc_4_7 = Arc(node_4, node_7, 0, 'x_3')
node_4.add_out_arc(arc_4_7)
node_7.add_in_arc(arc_4_7)
graph.add_node(node_7)


graph.add_new_layer()
node_8 = Node('8', [0])
arc_5_8_op1 = Arc(node_5, node_8, 0, 'x_4')
node_5.add_out_arc(arc_5_8_op1)
node_8.add_in_arc(arc_5_8_op1)
arc_5_8_op2 = Arc(node_5, node_8, 1, 'x_4')
node_5.add_out_arc(arc_5_8_op2)
node_8.add_in_arc(arc_5_8_op2)

arc_6_8 = Arc(node_6, node_8, 0, 'x_4')
node_6.add_out_arc(arc_6_8)
node_8.add_in_arc(arc_6_8)

arc_7_8 = Arc(node_7, node_8, 0, 'x_4')
node_7.add_out_arc(arc_7_8)
node_8.add_in_arc(arc_7_8)

graph.add_node(node_8)
