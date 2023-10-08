class MinMaxFunction:

    def __init__(self, n_variables, variable_ranges, function_operations, weights):
        self.n_variables = n_variables
        self.variable_ranges = variable_ranges
        self.function_operations = function_operations
        self.weights = weights

        self.create_variables()

    def create_variables(self):
        self.variables = []
        for i in range(self.n_variables):
            variable = Variable()
            variable.set_range(self.variable_ranges[i], "binary")
            self.variables.append(variable)

    
    def obtain_current_value(self):
        current_value = 0
        for i in range(self.n_variables):
            if not self.variables[i].is_variable_set():
                raise Exception("Variable " + str(i) + " is not set")
            
            current_value = self.math_operation(self.function_operations[i], current_value,
                                                self.weights[i] * self.variables[i].value)
        return current_value
        
    def math_operation(self, operation, value_one, value_two):
        if operation == "+":
            return value_one + value_two
        elif operation == "-":
            return value_one - value_two
        else:
            return None


class Variable:

    def __init__(self):
        self.value = None
        self.range = None

    def set_value(self, value):
        self.value = value

    def set_range(self, range, type):
        self.range = Range(range, type)

    def is_value_in_range(self, value):
        return self.range.in_range(value)
    
    def is_variable_set(self):
        return self.value != None
    

class Range:

    def __init__(self, range, type):
        self.range = range
        self.define_type(type)

    def define_type(self, type):
        if type == "between_two_values":
            self.in_range = self.between_two_values
        elif type == "binary":
            self.in_range = self.binary
        elif type == "in_list":
            self.in_range = self.in_list

    def between_two_values(self, value):
        return value >= self.range[0] and value <= self.range[1]
    
    def binary(self, value):
        return value == 0 or value == 1
    
    def in_list(self, value):
        return value in self.range
