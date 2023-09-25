
class Arc():

    def __init__(self, id_arc,out_node, in_node, variable_value, variable_id):
        self.id_arc = id_arc
        self.out_node = out_node
        self.in_node = in_node
        self.transicion_value = None
        self.variable_value = variable_value
        self.variable_id = variable_id
    
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
