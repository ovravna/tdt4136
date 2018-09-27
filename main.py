from ex2.Solver import Solver_String

if __name__ == '__main__':
	start = "abcdef"
	goal = "fcedab"

	a = Solver_String(start, goal)
	a.solve()

	for i in a.path:
		print(i)


