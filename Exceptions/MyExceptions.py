
class SameLenError(Exception):
    def __init__(self, message="Variables must have the same length"):
        self.message = message
        super().__init__(self.message)

class SameVariables(Exception):
    def __init__(self, message="Variables must be the same between dictionaries"):
        self.message = message
        super().__init__(self.message)

class MustBeIntegers(Exception):
    def __init__(self, message="Values must be integers"):
        self.message = message
        super().__init__(self.message)

class ConsistentDictionaryOfNeighbors(Exception):
    def __init__(self, message="Dictionary of neighbors must be consistent"):
        self.message = message
        super().__init__(self.message)