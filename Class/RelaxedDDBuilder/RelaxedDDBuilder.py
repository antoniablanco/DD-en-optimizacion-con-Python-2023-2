from Class.DDStructure.Node import Node
from Class.DDStructure.Arc import Arc
from Class.DDStructure.Graph import Graph

from Class.decorators.timer import timing_decorator


class RelaxedDDBuilder():
    '''
    Clase que construye un grafo de decisión relajado basado en un problema dado.
    '''

    @timing_decorator(enabled=False)
    def __init__(self, problem, max_width):
        '''
        Constructor de la clase Constructor de un grafo relajado.

        Parámetros:
        - problem: Objeto tipo problema para el cual se construirá el grafo.
        '''
        self._node_number = 1
        self.graph = None

        self._problem = problem
        self._variables = problem.ordered_variables
        self._variables_domain = problem.variables_domain
        self._max_width = max_width

        self._initialize_graph(problem.initial_state)
        
    def _initialize_graph(self, initial_state):
        '''
        Inicializa el grafo con un nodo raíz.

        Parámetros:
        - initial_state: Estado inicial del problema.
        '''
        node_root = Node(0, initial_state)
        self.graph = Graph(node_root)
    
    def get_decision_diagram(self, should_visualize):
        '''
        Retorna el grafo de decisión construido.

        Parámetros:
        - should_visualize: Booleano que indica si se debe visualizar la construcción del grafo.

        Retorna:
        - Graph: Objeto tipo grafo de decisión construido.
        '''
        for variable_id in range(len(self._variables)):
            self._create_new_layer(variable_id)
            self._merge_nodes_when_width_is_greater_than_w()
            self._print_graph(should_visualize)
        self._adjust_node_number()

        return self.graph
    
    def _create_new_layer(self, variable_id):
        '''
        Crea una nueva capa en el grafo para una variable dada.

        Parámetros:
        - variable_id: Índice de la variable para la cual se crea la nueva capa.
        '''
        self.graph.new_layer()
        self._create_new_nodes_in_the_new_layer(variable_id)

    def _create_new_nodes_in_the_new_layer(self, variable_id):
        '''
        Crea nodos en la nueva capa del grafo.

        Parámetros:
        - variable_id: Índice de la variable para la cual se crean nodos en la nueva capa.
        '''
        for existed_node in self.graph.structure[-2][:]:
            for variable_value in self._variables_domain[self._variables[variable_id]]:
                self._check_if_new_node_should_be_created(variable_value, existed_node, variable_id)
    
    def _check_if_new_node_should_be_created(self, variable_value, existed_node, variable_id):
        '''
        Verifica si debe crearse un nuevo nodo en la capa actual.

        Parámetros:
        - variable_value: Valor de la variable para la cual se verifica la creación del nuevo nodo.
        - existed_node: Nodo existente en la capa anterior.
        - variable_id: Índice de la variable para la cual se realiza la verificación.
        '''
        node_state, isFeasible = self._problem.transition_function(existed_node.state, self._variables[variable_id], variable_value)
        if isFeasible:
            if self._there_is_node_in_last_layer(variable_id):
                self._create_arcs_for_the_terminal_node(existed_node, variable_value, variable_id)
            else:
                self._create_rest_of_arcs(existed_node, variable_value, variable_id, node_state)
    
    def _there_is_node_in_last_layer(self, variable_id):
        '''
        Verifica si hay nodos en la última capa del grafo.

        Parámetros:
        - variable_id: Índice de la variable para la cual se realiza la verificación.

        Retorna:
        bool: True si hay nodos en la última capa, False en caso contrario.
        '''
        return self._variables[-1] == self._variables[variable_id] and self.graph.structure[-1] != []
    
    def _create_arcs_for_the_terminal_node(self, existed_node, variable_value, variable_id):
        '''
        Crea arcos para el nodo terminal en la última capa.

        Parámetros:
        - existed_node: Nodo existente en la capa anterior.
        - variable_value: Valor de la variable para la cual se crean los arcos.
        - variable_id: Índice de la variable para la cual se crean los arcos.
        '''
        terminal_node = self.graph.structure[-1][-1]
        self._create_arc_for_the_new_node(existed_node, terminal_node, variable_value, variable_id)
    
    def _create_rest_of_arcs(self, existed_node, variable_value, variable_id, node_state):
        '''
        Crea los arcos para un nodo que no se encuentra en la última capa.

        Parámetros:
        - existed_node: Nodo existente en la capa anterior.
        - variable_value: Valor de la variable para la cual se crean los arcos.
        - variable_id: Índice de la variable para la cual se crean los arcos.
        - node_state: Estado del nuevo nodo.
        '''
        nodo_existe, same_state_node = self._exist_node_with_same_state(node_state)
        if nodo_existe:
            self._create_arc_for_the_new_node(existed_node, same_state_node, variable_value, variable_id)
        else:
            node_created = Node(str(self._node_number), node_state)
            self._node_number += 1    
            self._create_arc_for_the_new_node(existed_node, node_created, variable_value, variable_id)
            self.graph.add_node(node_created)

    def _exist_node_with_same_state(self, node_state):
        '''
        Verifica si existe un nodo con el mismo estado en la misma capa.

        Parámetros:
        - node_state: Estado del nodo para el cual se realiza la verificación.

        Retorna:
        tuple: (bool, Node) - True si existe un nodo con el mismo estado, False y None en caso contrario.
        '''
        for node in self.graph.structure[-1]:
            if self._problem.equals(node.state, node_state):
                return True, node
        return False, None

    def _create_arc_for_the_new_node(self, existed_node, node_created, variable_value, variable_id):
        '''
        Crea un arco para un nodo ya existente.

        Parámetros:
        - existed_node: Nodo existente en la capa anterior.
        - node_created: Nuevo nodo creado.
        - variable_value: Valor de la variable para la cual se crea el arco.
        - variable_id: Índice de la variable para la cual se crea el arco.
        '''
        arc = Arc(existed_node, node_created, variable_value, self._variables[variable_id])
        existed_node.add_out_arc(arc)
        node_created.add_in_arc(arc)

    def _merge_nodes_when_width_is_greater_than_w(self):
        '''
        Realiza la fusión de nodos cuando el ancho es mayor que w.
        '''
        while self._width_is_greater_than_w():
            ordered_nodes = sorted(self.graph.structure[-1], 
            key=lambda node: self._problem.sort_key_nodes_to_merge(node.id_node))
            self._merge_nodes(ordered_nodes[0], ordered_nodes[1])

    def _width_is_greater_than_w(self):
        '''
        Verifica si el ancho del grafo es mayor que el ancho máximo permitido.
        '''
        return len(self.graph.structure[-1]) > self._max_width
    
    def _merge_nodes(self, node_to_remove, node_to_keep):
        '''
        Fusiona dos nodos.

        Parámetros:
        - node_one: Primer nodo a fusionar.
        - node_two: Segundo nodo a fusionar.
        '''

        self._redirect_in_arcs(node_to_remove, node_to_keep)
        self._change_new_state(node_to_remove, node_to_keep)
        self._delete_node(node_to_remove)
    
    def _redirect_in_arcs(self, node_to_remove, node_to_keep):
        '''
        Redirige los arcos de entrada de un nodo al otro nodo.

        Parámetros:
        - changin_nodes_ordered: Lista que contiene nodos en el orden deseado.
        '''
        for arc in node_to_remove.in_arcs:
            arc.in_node = node_to_keep
            if arc not in node_to_keep.in_arcs:
                node_to_keep.add_in_arc(arc)
    
    def _change_new_state(self, node_to_remove, node_to_keep):
        '''
        Cambia el estado del nuevo nodo.
        '''
        node_to_keep.state = self._problem.merge_operator(node_to_remove.state, node_to_keep.state)

    def _delete_node(self, node_to_remove):
        '''
        Elimina un nodo.

        Parámetros:
        - changin_nodes_ordered: Lista que contiene nodos en el orden deseado.
        '''
        self.graph.remove_node(node_to_remove)
        del node_to_remove

    def _adjust_node_number(self):
        '''
        Ajusta el número de nodos en el grafo.
        '''
        initial_node_number = 0
        for layer in self.graph.structure:
            for node in layer:
                node.id_node = str(initial_node_number)
                initial_node_number += 1

    def _print_graph(self, should_visualize):
        '''
        Imprime el grafo si se solicita la visualización.

        Parámetros:
        - should_visualize: Booleano que indica si se debe visualizar el grafo.
        '''
        if should_visualize:
            self._print()

    def _print(self):
        '''
        Imprime el contenido de cada capa del grafo.
        '''
        print("")
        for layer in self.graph.structure:
            print("------------------------------------------------------")
            for node in layer:
                in_arcs_str = ", ".join(str(arc) for arc in node.in_arcs)
                print(str(node) + "(" + in_arcs_str + ")", end=" ")
            print("")