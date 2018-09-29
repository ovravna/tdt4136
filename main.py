
from ex2.Solver import Solver
from ex2.State import Board_State, State


# Parse str to [[str]] board
def file_to_board(src) -> [[str]]:
	with open(src, 'r') as file:
		lines = file.readlines()
	return [[n for n in x if n != '\n'] for x in lines]


# Parse txt file to [[str]] board
def str_to_board(string_board: str) -> [[str]]:
	return [[n for n in x] for x in string_board.split('\n')]


if __name__ == '__main__':

	#runs for all boards
	for n in range(1, 3):
		for m in range(1, 5):
			b = file_to_board("ex2/boards/board-{}-{}.txt".format(n, m))

			state: State = Board_State(b)
			a = Solver(state, True)
			a.solve()
			print(a.prettify())  #prints pretty output



