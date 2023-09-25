from Class.Node import Node
from Class.Arc import Arc
from Class.Graph import Graph

# This class represents a path in a graph.
# A path is a list of nodes and arcs.
# The first element of the list is the initial node.

class Constructor():

    def __init__(self, problem):
        self.numero_nodo = 1
        self.Graph = None

        # Despues todas estas las obtengo directo del problem
        self.problem = problem
        self.dominio = problem.VariableNature
        self.variables = problem.orderedVariables
        self.initial_state = problem.initialState

        self.inicializar_grafo()

    def inicializar_grafo(self):
        node_r = Node("r", self.initial_state)
        self.Graph = Graph(node_r)
    
    def checking_nodes_state(self):
        lastLayer = self.Graph.structure[-1][:]
        for i, nodeOne in enumerate(lastLayer):
            for j, nodeTwo in enumerate(lastLayer):
                # Check if the indexes are different and nodeOne.state == nodeTwo.state
                if i < j and nodeOne.idNode != nodeTwo.idNode and nodeOne.state == nodeTwo.state:
                    self.merge_nodes(nodeOne, nodeTwo)

    def print_layer(self):
        print("------------------------------------------------------")
        print("")
        for layer in self.Graph.structure:
            for node in layer:
                in_arcs_str = ", ".join(str(arc.idArc) for arc in node.inArcs)  # Convert each Arc to a string
                print(node.idNode + "(" + in_arcs_str + ")", end=" ")
            print("")

    def verificar_factbilidad_layer(self):
        for node in self.Graph.structure[-1][:]:
            self.verificar_factibilidad_estado_un_nodo(node)

    def verificar_factibilidad_estado_un_nodo(self, node):
        if  not self.FactibilityFunction(node):
            for arc in node.inArcs:
                node.inArcs.remove(arc)
                del arc
            self.Graph.remove_node(node) # Eliminar el no factible
            del node

    def FactibilityFunction(self, node):
        #return verificar_factibilidad_estado(node)
        return (int(node.state[0]) <= 6)

    def get_state_node(self):
        # Aqui se deberia ocupar la que entrega el usuario
        input_state = input("Ingrese el estado del nodo: ")
        return input_state

    def get_transicion_value_arc(self):
        # Aqui se deberia ocupar la que entrega el usuario
        input_transicion_value = input("Ingrese el valor de la transicion: ")
        return input_transicion_value

    def get_node_changing(self, nodeOne, nodeTwo):
        current_layer = self.Graph.structure[self.Graph.actualLayer]
        if nodeOne in current_layer and nodeTwo in current_layer:
            if current_layer.index(nodeOne) > current_layer.index(nodeTwo):
                return (nodeOne, nodeTwo)  
            else:
                return (nodeTwo, nodeOne)
        
    def merge_nodes(self, nodeOne, nodeTwo):
        nodes = list(self.get_node_changing(nodeOne, nodeTwo))
        changinNodes = [nodes[0], nodes[1]]
        
        for arc in changinNodes[0].inArcs:
            arc.inNode = changinNodes[1]
            arc.idArc = "arc_" + arc.outNode.idNode + "_" + changinNodes[1].idNode
            changinNodes[1].add_in_arc(arc)

        indexNode, indexLayer = self.Graph.get_index_node(changinNodes[0])

        self.Graph.remove_node(changinNodes[0])
        del changinNodes[0]

        self.numero_nodo -= 1
        self.actualizar_nombre_nodos(indexNode, indexLayer)

    def actualizar_nombre_nodos(self, indexNode, indexLayer):
        # Actualizar nombres de nodos a partir del nodo_se_queda
        for i, node in enumerate(self.Graph.structure[indexLayer]):
            if i > indexNode:
                node.idNode = "u" + str(int(node.idNode[1:]) - 1)
                for arc in node.inArcs:
                    nuevo_id_arc = "arc_" + arc.outNode.idNode + "_" + arc.inNode.idNode
                    if arc.idArc != nuevo_id_arc:
                        arc.idArc = nuevo_id_arc
    
    def merge_terminal_node(self):
        lastLayer = self.Graph.structure[-1][:]
        final_node = Node("t", [])
        self.Graph.add_final_node(final_node)

        for nodeOne in lastLayer:
            self.merge_nodes(nodeOne, final_node)
    
    def get_decision_diagram(self):
        for variable in range(len(self.variables)):
            self.Graph.new_layer()
            for existedNode in self.Graph.structure[-2][:]:
                for path in self.dominio:
                    estado = self.get_state_node()
                    path_nodo = [estado]
                    nodeCreated = Node("u" + str(self.numero_nodo), path_nodo)
                    if self.FactibilityFunction(nodeCreated):
                        self.numero_nodo += 1    
                        valor_transicion = self.get_transicion_value_arc()
                        arc = Arc("arc_" + str(existedNode.idNode) + "_" + str(nodeCreated.idNode), existedNode, nodeCreated, valor_transicion, path)
                        existedNode.add_out_arc(arc)
                        nodeCreated.add_in_arc(arc)
                        self.Graph.add_node(nodeCreated)
            self.checking_nodes_state()
            self.print_layer()
        
        self.merge_terminal_node()
        self.print_layer()

        return self.Graph
