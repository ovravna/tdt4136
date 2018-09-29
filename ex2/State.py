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


#cost of board locations
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

#Board colors
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

	#finds start point, goal point and dimensions
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

	#calculates cartesian distance
	def get_dist(self, a: Tuple) -> float:
		return math.sqrt((self.goal.value[0] - a[0])**2
		                 + (self.goal.value[1] - a[1])**2)

	# Generates children on the cardinal directions with in the board
	def generate_children_of(self, node: Node):

		x0, y0 = node.value # coordinates of node

		for j in range(-1, 2):
			for i in range(-1, 2):

				if bool(i) == bool(j): # removes non cardinal children
					continue

				#coordinates of child
				x = x0 + i
				y = y0 + j

				#Removes children that are not with in the board
				if x not in range(*self.x_dim):
					continue
				if y not in range(*self.y_dim):
					continue


				node.children\
					.append(Node((x, y), node, self.get_dist((x, y))))


