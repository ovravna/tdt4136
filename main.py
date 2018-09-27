from ex2.Node import Node
from ex2.Solver import Solver
from ex2.State import String_State, Board_State, State

if __name__ != '__main__':
	start = "abcdef"
	goal = "fcedab"

	initial_node: Node = Node(start, None, 0)


	a = Solver(state=String_State(start, goal))
	a.solve()

	for i in a.path:
		print(i)


def str_to_board(string_board: str) -> [[str]]:
	return [[n for n in x] for x in string_board.split('\n')]


if __name__ == '__main__':
	b = str_to_board("""....................
....................
.........######.....
...........A..#..B..
.........######.....
....................
....................""")

	state: State = Board_State(b)
	a = Solver(state)
	a.solve()
	print("Path:")
	for i in a.path:
		print(i)
	print(a.prittify())



