class Node():
    '''
    Clase que representa un nodo en un grafo dirigido acíclico.
    '''

    def __init__(self, id_node, state):
        '''
        Constructor de la clase Node.

        Parámetros:
        - id_node(int): Identificador único del nodo.
        - state(): Estado asociado al nodo.
        '''
        self.id_node = id_node
        self.state = state
        self.in_arcs = []
        self.out_arcs = []
    
    def __str__(self):
        '''
        Retorna:
        str: Representación de cadena del objeto Node.
        '''
        return "u_"+str(self.id_node)+" "+str(self.state)+""
    
    def add_in_arc(self, arc):
        '''
        Agrega un arco entrante a la lista de in_arcs.

        Parámetros:
        - arc: Objeto de la clase Arc que representa el arco entrante.
        '''
        if arc not in self.in_arcs:
            self.in_arcs.append(arc)
    
    def add_out_arc(self, arc):
        '''
        Agrega un arco saliente a la lista de out_arcs.

        Parámetros:
        - arc: Objeto de la clase Arc que representa el arco saliente.
        '''
        if arc not in self.out_arcs:
            self.out_arcs.append(arc)
    
    def remove_in_arc(self, arc):
        '''
        Elimina un arco entrante de la lista de in_arcs.

        Parámetros:
        - arc: Objeto de la clase Arc que representa el arco entrante a eliminar.
        '''
        if arc in self.in_arcs:
            self.in_arcs.remove(arc)

    def remove_out_arc(self, arc):
        '''
        Elimina un arco saliente de la lista de out_arcs.

        Parámetros:
        - arc: Objeto de la clase Arc que representa el arco saliente a eliminar.
        '''
        if arc in self.out_arcs:
            self.out_arcs.remove(arc)
