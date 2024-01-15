# Decision Diagram Program

This program provides a versatile implementation of Decision Graphs for solving optimization problems. The following guide will help you use the program.

## Requisites

Make sure you have in your system

* python > 3.11
* networkx
* matplotlibsd

For a complete use of the program, it is recommended to have a tool that can read documents with a .gml extension. yED is a suitable program for this purpose.

## Installation

Clone this repository and navigate to the project directory to implement the main program. To review examples, go to the '/Examples/' directory, where you'll find three folders with different examples. In each of them, execute the one with 'main' at the end of its name.

## Getting Started

First should proceed to the construction of a **Problem** class, which must inherit from  **AbstractProblem** . It is crucial to define the following functions for this class:

* **equals:** Takes two states as input and should give as output a boolean value indicating whether they are equal or not.
* **transition_function:** Takes as inputs a previous state, a variable identifier (e.g., "x_2"), and the domain this variable takes (e.g., "1"). It outputs a new state and a boolean value indicating whether the state is feasible or not.

If you want to obtain the restricted diagram, it is necessary to implement the following function when constructing your **Problem** class.

* **get_priority_for_discard_node:** Takes the state of a node as input and outputs a number representing the priority for discarding the node.

Furthermore, to obtain the relaxed diagram, it is necessary to add the following two functions in the **Problem** class.

* **get_priority_for_merge_nodes:** Takes a state and the ID of a node as inputs and outputs a number representing the priority for merging the node with others.
* **merge_operator:** Takes two states, each one from a node that is going to merge, as inputs. It outputs a new state for the merged nodes..

Once this class is built, it is essential to create an instance of it to be passed to the "DD" class. In this, you'll find functions to create, reduce, restrict, relax and visualize a diagram, as well as obtain a copy of it.

Finally, to obtain the problem's solution, create an instance of the **ObjectiveFunction** class, to which you pass the DD object containing the graph. Within this function, you can assign and solve the objective function.

## Features

#### Create Decision Diagram

It is the initial and necessary feature for all the following ones; that's why it is included when creating an instance of the DD class. To do this, you need to provide an instance of the created Problem class.

#### Create Reduce Decision

To create the reduced decision diagram, is necesary use *create_reduce_decision_diagram()* from the **DD** class, which transforms the graph class object saved when creating the diagram into its reduced form. This new version is then stored within the **DD** class.

#### Create Restricted Decision

To create the restricted decision diagram, is necesary use *create_restricted_decision_diagram()* from the **DD** class, which transforms the graph class object saved when creating the diagram into its restricted form. This new version is then stored within the **DD** class.

#### Create Relax Decision

To create the relax decision diagram, is necesary use *create_relax_decision_diagram()* from the **DD** class, which transforms the graph class object saved when creating the diagram into its relax form. This new version is then stored within the **DD** class.

#### Print Decision Diagram

For a quick visualization of the created diagram, can be use the *print_decision_diagram()* method of the **DD** class. It's important to note that this method uses the networkx library; therefore, it has a limitation of 5 different line types. If you have a variable domain greater than this, the design of the arcs will be repeated.

#### Export Decision Diagram

To export the created decision diagram, whether it's reduced or in its original format, should be use the *export_graph_file()* method of the **DD** class. This generates a *.gml* file that can be visualized in programs such as *yED.*

#### Get a Copy Of the Decision Diagram

To obtain a copy of the DD instance without it being a pointer to the original object, you should use the *get_decision_diagram_graph_copy()* method of the **DD** class. This feature can be useful for testing different constructors or functions to solve the diagram.

#### Solve the Decision Diagram

The first step to use this feature is to create an instance of the ObjectiveFunction, providing the dd_instance instance created earlier. Subsequently, it is necessary to create an instance of the algorithm to be used for solving the graph, which should receive a list with the weights of each variable in the objective function, and a string representing whether it is to maximize or minimize. The string values 'min' or 'max' can be used. For example, LinearObjectiveDP or SchedulingObjective. Finally, you should use the *SetObjectiveFunction()* method of the **ObjectiveFunction** class, providing the instance of the created algorithm. Subsequently, you can obtain the solution by using *solve_dd()* of the same class.

#### Get the Time of the Algoritms

If it's want to get the time taken by the algorithms for creating the diagram or another of its forms, you need to use the *get_dd_builder_time()* or *get_TYPE_constructor_time()* methods of the **DD** class, where TYPE represent the type of graph that its wanted, for example relax, restricted or reduce. On the other hand, to obtain the objective function time, you should use *get_time()* from the **ObjectiveFunction** class.

## Examples

For a more comprehensive understanding of these classes, it is recommended to thoroughly review the examples available in the **"/Examples/"** folder within the code, and execute **Knapsack/KnapsackMain** *or* **IndependentSet/IndependentSetMain.** These examples are generic and open for testing different values. In light of the above, the examples will be explained below.

#### Knapsack

Within the **KnapsackMain** file, it can be noticed that it is a generalized version of a linear problem. For this reason, it is possible to input the weights of the variables in the different constraints. This should be done in the *matrix_of_weight* parameter, and it is also necessary to provide the value on the right side of the constraints in the *right_side_of_restrictions* parameter. With these two values, an instance of Knapsack can be created. However, to generate a decision diagram, it is necessary to provide the initial state in *initial_state* and the variables with their domain in *variables.* After defining all the parameters and delivering them in the creation of an instance of the KnapsackProblem, it is ready to test the various features that were explained earlier. Importantly, it should be noted that there are some checks in place to ensure there is no inconsistency in the provided data.

#### IndependentSet

Similar to the previous case, it can be observed that in the IndependentSetMain file, it corresponds to a generalization of the IndependentSet problem. Therefore, it is possible to test different values. To do so, it is necessary to provide a dictionary in which the *key* is the variable's ID, and the *value* corresponds to a list of all nodes, that can be reached in a single arc, formatted as integers. Once the variables are selected to instantiate the IndependentSet, it is necessary to create the variables to build a decision diagram. These include *initial_state* on one hand and, on the other hand, the variable IDs with their domain in *variables.* After providing all the parameters to the instance of the constructed problem class, you can test the other features.

#### SetCovering

This example represents a generalization of the set covering problem, allowing for different values to test various cases. To construct it, various values need to be provided. First, the initial state should be a list containing numbers representing the number of constraints to be given, for example, "[1,2,3]". Additionally, a dictionary of variables along with their domains must be provided. Specifically for this problem, the `right_side_of_restrictions` is the minimum value for each constraint, associated through their positions. Lastly, `matrix_of_weight` is a list of lists where the values represent the probability of each variable (associated by position) being within the constraint. After providing all these parameters to the instance of the constructed problem class, you can test the other features.

## Test Casses

Test cases have been created for the three examples explained earlier. These test all the implemented features and can be used to verify that different changes implemented continue to provide correct responses.

## Extending the Code

It is important to emphasize that all classes along with their modules have been documented for a more detailed understanding. This can be useful if it's want to create new objective functions or diagram constructors, which are expected to follow the same directory structure.
