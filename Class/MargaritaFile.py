class MargaritaFile:

    def __init__(self, file_name, graph):
        self.file_name = file_name
        self.graph = graph

        self.create_gml_file()
        self.start_file()
        self.add_nodes()
        self.end_file()

    def create_gml_file(self):

        self.file = open(f"{self.file_name}.gml", 'w')

    def start_file(self):
        self.file.write("graph [\n")
        self.file.write("\tdirected 1\n")
        self.file.write("\thierarchic 1")

    def end_file(self):
        self.file.write("\n]")

    def add_nodes(self):
        arcs = []
        for layer in self.graph.structure:
            for node in layer:
                self.add_node(node)
                arcs += node.out_arcs
        self.add_arcs(arcs)

    def add_arcs(self, arcs):
        for arc in arcs:
            self.add_arc(arc)

    def add_node(self, node):
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

    def add_arc(self, arc):
        self.file.write(f"\nedge [\n")
        if arc.out_node.id_node == 'r':
            self.file.write(f"\tsource 0\n")
        else:
            self.file.write(f"\tsource {arc.out_node.id_node}\n")

        if arc.in_node.id_node == 't':
            self.file.write(f"\ttarget 500\n")
        else:
            self.file.write(f"\ttarget {arc.in_node.id_node}\n")
        self.file.write(f"\tlabel \"{arc.transicion_value}\"\n")
        self.file.write("\tgraphics [\n")
        if arc.variable_value == 0:
            self.file.write(f"\tfill \"#808080\" 		targetArrow \"standard\"	 style	\"dashed\"	 ]\n")
        else:
            self.file.write(f"\tfill \"#000000\" 		targetArrow \"diamond\"	 	 ]\n")
        self.file.write(f"]")