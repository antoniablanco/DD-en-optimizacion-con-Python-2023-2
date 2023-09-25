
class Arc():

    def __init__(self, idArc,outNode, inNode, variableValue, variableId):
        self.idArc = idArc
        self.outNode = outNode
        self.inNode = inNode
        self.transicionValue = None
        self.variableValue = variableValue
        self.variableId = variableId
    
    @property
    def outNode(self):
        return self._outNode

    @outNode.setter
    def outNode(self, value):
        self._outNode = value

    @property
    def inNode(self):
        return self._inNode

    @inNode.setter
    def inNode(self, value):
        self._inNode = value

    @property
    def transicionValue(self):
        return self._transicionValue

    @transicionValue.setter
    def transicionValue(self, value):
        self._transicionValue = value

    @property
    def variableValue(self):
        return self._variableValue

    @variableValue.setter
    def variableValue(self, value):
        self._variableValue = value

    @property
    def variableId(self):
        return self._variableId

    @variableId.setter
    def variableId(self, value):
        self._variableId = value
