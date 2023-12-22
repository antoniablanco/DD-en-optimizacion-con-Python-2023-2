from Class.DDStructure.Node import Node
from Class.DDStructure.Arc import Arc
from Class.DDStructure.Graph import Graph

from Class.decorators.timer import timing_decorator

class GraphFile:
    '''
    Clase que se encarga de generar un archivo GML (Graph Modeling Language)
    para representar un grafo jerárquico dirigido con nodos y arcos.
    '''

    @timing_decorator(enabled=False)
    def __init__(self, file_name: str, graph: Graph):
        '''
        Constructor de la clase GraphFile.

        Parámetros:
        - file_name (str): Nombre del archivo GML a ser creado.
        - graph (Graph): Objeto de la clase Graph que se va a representar en el archivo GML.
        '''
        self.file_name = file_name
        self.graph = graph

        self._create_gml_file()
        self.is_graph_binary = self._check_if_graph_is_binary()
        self._start_file()
        self._add_nodes_and_arcs()
        self._end_file()

    def _create_gml_file(self):
        '''
        Crea el archivo GML y abre el archivo para escritura.
        '''
        self.file = open(f"{self.file_name}.gml", 'w')

    def _start_file(self):
        '''
        Inicia la estructura del archivo GML con la información del grafo.
        '''
        self.file.write("graph [\n")
        self.file.write("\tdirected 1\n")
        self.file.write("\thierarchic 1")

    def _add_nodes_and_arcs(self):
        '''
        Agrega nodos al archivo GML, junto con la información de sus arcos salientes.
        '''
        arcs = []
        for layer in self.graph.structure:
            for node in layer:
                self._add_node(node)
                arcs += node.out_arcs      
        self._add_arcs(arcs)
            
    def _check_if_graph_is_binary(self) -> bool:
        '''
        Determina si un grafo es binario, es decir, si todos sus variables son binarios.

        Retorna:
        - True si el grafo es binario.
        - False si el grafo no es binario.
        '''

        for layer in self.graph.structure:
            for node in layer:
                if not self._is_node_binary(node):
                    return False
                
        return True
                

    def _is_node_binary(self, node: Node) -> bool:
        '''
        Determina si un nodo es binario, es decir, si sus arcos salientes son de valor 0 o 1.

        Parámetros:
        - node (Node): Objeto de la clase Node que posee arcos con valor de variable.

        Retorna:
        - True si el nodo es binario.
        - False si el nodo no es binario.
        '''
        for arc in node.out_arcs:
            if arc.variable_value != 0 and arc.variable_value != 1:
                return False
            
        return True

    
    def _add_node(self, node: Node) -> None:
        '''
        Agrega información de un nodo al archivo GML.

        Parámetros:
        - node (Node): Objeto de la clase Node que se va a agregar al archivo GML.
        '''
        self.file.write(f"\n node [\n")
        if node.id_node == 'r':
            self.file.write(f"\t id 0\n")
        elif node.id_node == 't':
            self.file.write(f"\t id 500\n")
        else:
            self.file.write(f"\t id {node.id_node}\n")
        
        self.file.write(f"\t label \"{node.id_node}\"\n")
        self.file.write(" \tgraphics [\n")
        self.file.write(f"\t type \"circle\"\n")
        self.file.write(f"\t hasFill 0\n")
        self.file.write("\t w 90.0   h 110.0  ]\n")
        self.file.write(f"]")

    def _add_arcs(self, arcs: list[Arc]) -> None:
        '''
        Agrega arcos al archivo GML.

        Parámetros:
        - arcs (list): Lista de objetos Arc a ser agregados al archivo GML.
        '''
        for arc in arcs:
            self._add_arc(arc)

    def _add_arc(self, arc: Arc) -> None:
        '''
        Agrega información de un arco al archivo GML.

        Parámetros:
        - arc (Arc): Objeto de la clase Arc que se va a agregar al archivo GML.
        '''
        self.file.write(f"\nedge [\n")
        self._add_arc_source(arc)
        self._add_arc_target(arc)

        if not self.is_graph_binary:
            self._add_arc_label(arc)


        self._add_arc_graphics(arc)
        self.file.write(f"]\n")


    def _add_arc_source(self, arc: Arc) -> None:
        if arc.out_node.id_node == 'r':
            self.file.write(f"\tsource 0\n")
        else:
            self.file.write(f"\tsource {arc.out_node.id_node}\n")

    def _add_arc_label(self, arc: Arc) -> None:
        self.file.write(f"\tlabel \"{arc.variable_value}\"\n")

    def _add_arc_target(self, arc: Arc) -> None:
        if arc.in_node.id_node == 't':
            self.file.write(f"\ttarget 500\n")
        else:
            self.file.write(f"\ttarget {arc.in_node.id_node}\n")

    def _add_arc_graphics(self, arc: Arc) -> None:
        self.file.write("\tgraphics [\n")

        if self.is_graph_binary:
            self._add_binary_arc_graphics(arc)

        else:
            self._add_normal_arc_graphics(arc)

        self.file.write(f"]")


    def _add_normal_arc_graphics(self, arc: Arc) -> None:
        self.file.write(f"\tfill \"#000000\" 		targetArrow \"standard\"	 	 \n")


    def _add_binary_arc_graphics(self, arc: Arc) -> None:
        if arc.variable_value == 0:
            self.file.write(f"\tfill \"#808080\" 		targetArrow \"standard\"	 style	\"dashed\"	 \n")
        else:
            self.file.write(f"\tfill \"#000000\" 		targetArrow \"diamond\"	 	 \n")
    
    def _end_file(self):
        '''
        Finaliza la estructura del archivo GML.
        '''
        self.file.write("\n]")