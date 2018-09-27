import math
from typing import Tuple

from colors.colors import colors
from ex2 import Node
from ex2.Node import Node


class State:

	def __init__(self):
		self.start: Node = None
		self.goal: Node = None

	def initial_node(self) -> Node:
		return Node(self.start.value, None, 0)

	def get_dist(self, a) -> int:
		return 0

	def generate_children_of(self, node: Node):
		pass



Board = {
	"A": -3,
	"B": -2,
	"#": -1,
	".": 1,
	"w": 100,
	"m": 50,
	"f": 10,
	"g": 5,
	"r": 1,
}

Colors = {
	"A": (colors.bg.orange, colors.fg.black),
	"B": (colors.bg.orange, colors.fg.black),
	"#": colors.bg.lightgrey,
	".": colors.bg.black,
	"w": colors.bg.blue,
	"m": colors.bg.black,
	"f": colors.bg.green,
	"g": colors.bg.cyan,
	"r": colors.bg.lightgrey,



}

class Board_State(State):

	def __init__(self, board: [[str]]):
		super().__init__()

		self.board: [[str]] = board
		self.__parse_board()

		print(self.start)
		print(self.goal)
		print(self.get_dist(self.start.value))
		self.generate_children_of(self.start)
		print([n.value for n in self.start.children])
		print(self.x_dim, self.y_dim)



	def __parse_board(self):
		for y in range(len(self.board)):
			for x in range(len(self.board[y])):
				elem = self.board[y][x]
				if elem in Board:
					if Board[elem] == -3:
						self.start: Node = Node((x, y), None, 0)
					if Board[elem] == -2:
						self.goal: Node= Node((x, y), None, 0)

		self.x_dim = (0, len(self.board[0]))
		self.y_dim = (0, len(self.board))

	def get_dist(self, a: Tuple) -> float:
		return math.sqrt((self.goal.value[0] - a[0])**2  + (self.goal.value[1] - a[1])**2)

	def generate_children_of(self, node: Node):

		x0 = node.value[0]
		y0 = node.value[1]
		for j in range(-1, 2):
			for i in range(-1, 2):
				if bool(i) == bool(j):
					continue
				x = x0 + i
				y = y0 + j
				if x not in range(*self.x_dim):
					continue
				if y not in range(*self.y_dim):
					continue



				node.children\
					.append(Node((x, y), node, self.get_dist((x, y))))

class String_State(State):

	def __init__(self, start: str, goal: str):
		super().__init__()

		self.start: str = start
		self.goal: str = goal



	def get_dist(self, a: str) -> int:
		if a == self.goal:
			return 0
		dist: int = 0
		for i in range(len(self.goal)):
			letter = self.goal[i]
			dist += abs(i - a.index(letter))
		return dist

	def generate_children_of(self, node: Node):
		if node.children:
			return
		for i in range(len(self.goal) - 1):
			val = node.value
			val = val[:i] + val[i+1] + val[i] + val[i + 2:]
			child = Node(val, node, self.get_dist(val))
			node.children.append(child)


