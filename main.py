from ex2.Node import Node_String
from ex2.Solver import Solver

if __name__ == '__main__':
	start = "abcdef"
	goal = "fcedab"

	a = Solver(Node_String(start, None, start, goal))
	a.solve()

	for i in a.path:
		print(i)


