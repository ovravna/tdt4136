from ex2 import Node
from ex2.Node import Node_String
from ex2.Solver import Solver
from ex2.State import State

if __name__ == '__main__':
	start = "abcdef"
	goal = "fcedab"

	initial_node: Node = Node_String(start, None, 0)

	state = State(start, goal)
	a = Solver(initial_node, state)
	a.solve()

	for i in a.path:
		print(i)


