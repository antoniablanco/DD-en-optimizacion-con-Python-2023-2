import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)

from Class.DDStructure.Node import Node
from Class.DDStructure.Arc import Arc
from Class.DDStructure.Graph import Graph

node_0 = Node('0', [1,2,3,4,5])
graph = Graph(node_0)

# Crear la segunda capa de nodos
graph.new_layer()
node_1 = Node('1', [2, 3, 4, 5])
arc_0_1 = Arc(node_0, node_1, 0, 'x_1')
node_0.add_out_arc(arc_0_1)
node_1.add_in_arc(arc_0_1)
graph.add_node(node_1)

node_2 = Node('2', [4, 5])
arc_0_2 = Arc(node_0, node_2, 1, 'x_1')
node_0.add_out_arc(arc_0_2)
node_2.add_in_arc(arc_0_2)
graph.add_node(node_2)

graph.new_layer()
node_3 = Node('3', [5])
arc_1_3 = Arc(node_1, node_3, 1, 'x_2')
node_1.add_out_arc(arc_1_3)
node_3.add_in_arc(arc_1_3)
graph.add_node(node_3)

node_4 = Node('4', [4, 5])
arc_2_4 = Arc(node_2, node_4, 0, 'x_2')
node_2.add_out_arc(arc_2_4)
node_4.add_in_arc(arc_2_4)
graph.add_node(node_4)


graph.new_layer()
node_5 = Node('5', [5])
arc_3_5 = Arc(node_3, node_5, 0, 'x_3')
node_5.add_in_arc(arc_3_5)
node_3.add_out_arc(arc_3_5)
graph.add_node(node_5)

node_6 = Node('6', [4, 5])
arc_4_6 = Arc(node_4, node_6, 0, 'x_3')
node_4.add_out_arc(arc_4_6)
node_6.add_in_arc(arc_4_6)
graph.add_node(node_6)

# Crear la quinta capa de nodos
graph.new_layer()
node_7 = Node('7', [5])
arc_5_7 = Arc(node_5, node_7, 0, 'x_4')
node_5.add_out_arc(arc_5_7)
node_7.add_in_arc(arc_5_7)
arc_6_7 = Arc(node_6, node_7, 0, 'x_4')
node_6.add_out_arc(arc_6_7)
node_7.add_in_arc(arc_6_7)
graph.add_node(node_7)

node_8 = Node('8', [])
arc_6_8 = Arc(node_6, node_8, 1, 'x_4')
node_6.add_out_arc(arc_6_8)
node_8.add_in_arc(arc_6_8)
graph.add_node(node_8)

# Crear la sexta capa de nodos
graph.new_layer()
node_9 = Node('9', [])
arc_7_9_1 = Arc(node_7, node_9, 0, 'x_5')
node_7.add_out_arc(arc_7_9_1)
node_9.add_in_arc(arc_7_9_1)
arc_7_9_2 = Arc(node_7, node_9, 1, 'x_5')
node_7.add_out_arc(arc_7_9_2)
node_9.add_in_arc(arc_7_9_2)
arc_8_9 = Arc(node_8, node_9, 0, 'x_5')
node_8.add_out_arc(arc_8_9)
node_9.add_in_arc(arc_8_9)
graph.add_node(node_9)


