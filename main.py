from colors.colors import colored, colors
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

def file_to_board(src):
	with open(src, 'r') as file:
		lines = file.readlines()
	return [[n for n in x if n != '\n'] for x in lines]


def str_to_board(string_board: str) -> [[str]]:
	return [[n for n in x] for x in string_board.split('\n')]


if __name__ == '__main__':
# 	b = str_to_board("""....................
# ....................
# .........######.....
# ...........A..#..B..
# .........######.....
# ....................
# ....................""")
# 	print(colored("kake", colors.bg.blue, colors.fg.red), "ninja")



	b = file_to_board("ex2/boards/board-2-4.txt")
	print(b)

	state: State = Board_State(b)
	a = Solver(state)
	a.solve()
	print("Path:")
	for i in a.path:
		print(i)
	print(a.prettify())



