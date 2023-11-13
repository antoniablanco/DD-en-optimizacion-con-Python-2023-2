
class Arc():
    '''
    Clase que representa una estructura de los arcos. 
    '''

    def __init__(self, out_node, in_node, variable_value, variable_id):
        '''
        Constructor de la clase Arc.

        Parámetros:
        - out_node(Node): Nodo de salida del arco.
        - in_node(Node): Nodo de entrada del arco.
        - variable_value(int): Valor de la variable asociada al arco.
        - variable_id(string): Identificador único de la variable asociada al arco.
        '''
        self.out_node = out_node
        self.in_node = in_node
        self.variable_value = variable_value
        self.variable_id = variable_id
    
    def __str__(self) -> str:
        '''
        Retorna:
        str: Representación de cadena del objeto Arc.
        '''
        return "arc_" + str(self.out_node.id_node) + "_" + str(self.in_node.id_node)
    
    '''
    Los siguientes métodos son getters y setters de los atributos de la clase Arc.
    '''
    @property
    def out_node(self):
        return self._out_node

    @out_node.setter
    def out_node(self, value):
        self._out_node = value

    @property
    def in_node(self):
        return self._in_node

    @in_node.setter
    def in_node(self, value):
        self._in_node = value

    @property
    def transicion_value(self):
        return self._transicion_value

    @transicion_value.setter
    def transicion_value(self, value):
        self._transicion_value = value

    @property
    def variable_value(self):
        return self._variable_value

    @variable_value.setter
    def variable_value(self, value):
        self._variable_value = value

    @property
    def variable_id(self):
        return self._variable_id

    @variable_id.setter
    def variable_id(self, value):
        self._variable_id = value
