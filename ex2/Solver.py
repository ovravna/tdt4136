from queue import PriorityQueue

from colors.colors import *
from ex2 import State
from ex2.Node import Node
from ex2.State import Board, Colors


class Solver:

	def __init__(self, state: State, cartesian_flag: bool = False):
		self.cartesian_flag: bool = cartesian_flag
		self.state: State = state
		self.path = []
		self.visitQueue = []
		self.priorityQueue = PriorityQueue()
		self.node: Node = state.initial_node()

	def solve(self):

		count: int = 0
		self.priorityQueue.put((0, count, self.node)) #initial state


		while not self.path and self.priorityQueue.qsize():

			closestChild: Node = self.priorityQueue.get()[2] #gets child with highest priority, that is lowest heuristic + node cost
			self.state.generate_children_of(closestChild)
			self.visitQueue.append(closestChild.value)

			child: Node
			for child in closestChild.children:

				if child.value in self.visitQueue: # Checks if node is visited
					continue

				x, y = child.value #coordinates
				board_val = Board[self.state.board[y][x]] #cost of next state

				if board_val == -1: #wall or non reachable state
					continue

				if child.dist == 0: #Goal state reached
					self.path = child.path #solution path
					break

				count += 1 #counter for secondary priority in priorityQueue

				#Add heuristic and board weight as priority value
				self.priorityQueue.put((board_val + (child.dist if self.cartesian_flag else 0), count, child))
		if not self.path:
			print("failed...")
		return self.path

	# return pretty string of board with path
	def prettify(self):
		def pretty_colored(key: str, in_path: bool):
			k = colored("*", colors.fg.red) if in_path else " "
			if Board[key] in (-3, -2):
				k = key
			return colored(k, *Colors[key])

		res = "\n"
		for y in range(len(self.state.board)):
			for x in range(len(self.state.board[y])):
				res += pretty_colored(self.state.board[y][x],
				               in_path=(x, y) in self.path[1:-1])
			res += "\n"
		return res


