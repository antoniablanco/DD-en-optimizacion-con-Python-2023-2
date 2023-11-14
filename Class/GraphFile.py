class GraphFile:
    '''
    Clase que se encarga de generar un archivo GML (Graph Modeling Language)
    para representar un grafo jerárquico dirigido con nodos y arcos.
    '''

    def __init__(self, file_name, graph):
        '''
        Constructor de la clase GraphFile.

        Parámetros:
        - file_name (str): Nombre del archivo GML a ser creado.
        - graph (Graph): Objeto de la clase Graph que se va a representar en el archivo GML.
        '''
        self.file_name = file_name
        self.graph = graph

        self.create_gml_file()
        self.start_file()
        self.add_nodes()
        self.end_file()

    def create_gml_file(self):
        '''
        Crea el archivo GML y abre el archivo para escritura.
        '''
        self.file = open(f"{self.file_name}.gml", 'w')

    def start_file(self):
        '''
        Inicia la estructura del archivo GML con la información del grafo.
        '''
        self.file.write("graph [\n")
        self.file.write("\tdirected 1\n")
        self.file.write("\thierarchic 1")

    def add_nodes(self):
        '''
        Agrega nodos al archivo GML, junto con la información de sus arcos salientes.
        '''
        arcs = []
        for layer in self.graph.structure:
            for node in layer:
                self.add_node(node)
                arcs += node.out_arcs
        self.add_arcs(arcs)
    
    def add_node(self, node):
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

    def add_arcs(self, arcs):
        '''
        Agrega arcos al archivo GML.

        Parámetros:
        - arcs (list): Lista de objetos Arc a ser agregados al archivo GML.
        '''
        for arc in arcs:
            self.add_arc(arc)

    def add_arc(self, arc):
        '''
        Agrega información de un arco al archivo GML.

        Parámetros:
        - arc (Arc): Objeto de la clase Arc que se va a agregar al archivo GML.
        '''
        self.file.write(f"\nedge [\n")
        if arc.out_node.id_node == 'r':
            self.file.write(f"\tsource 0\n")
        else:
            self.file.write(f"\tsource {arc.out_node.id_node}\n")

        if arc.in_node.id_node == 't':
            self.file.write(f"\ttarget 500\n")
        else:
            self.file.write(f"\ttarget {arc.in_node.id_node}\n")

        self.file.write("\tgraphics [\n")
        if arc.variable_value == 0:
            self.file.write(f"\tfill \"#808080\" 		targetArrow \"standard\"	 style	\"dashed\"	 ]\n")
        else:
            self.file.write(f"\tfill \"#000000\" 		targetArrow \"diamond\"	 	 ]\n")
        self.file.write(f"]")
    
    def end_file(self):
        '''
        Finaliza la estructura del archivo GML.
        '''
        self.file.write("\n]")