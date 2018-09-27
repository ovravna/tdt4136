from queue import PriorityQueue

from colors.colors import *
from ex2 import State
from ex2.Node import Node
from ex2.State import Board, Colors


class Solver:

	def __init__(self, state: State):
		self.state: State = state
		self.path = []
		self.visitQueue = []
		self.priorityQueue = PriorityQueue()
		self.node: Node = state.initial_node()

	def solve(self):

		count: int = 0
		self.priorityQueue.put((0, count, self.node))

		while not self.path and self.priorityQueue.qsize():
			closestChild: Node = self.priorityQueue.get()[2]
			self.state.generate_children_of(closestChild)
			self.visitQueue.append(closestChild.value)

			child: Node
			for child in closestChild.children:
				if child.value not in self.visitQueue:

					x, y = child.value
					board_val = Board[self.state.board[y][x]]
					if board_val == -1:
						continue

					if child.dist == 0:
						self.path = child.path
						break

					count += 1
					self.priorityQueue.put((child.dist + board_val, count, child))
		if not self.path:
			print("failed...")
		return self.path

	def prettify(self):
		def pretty_colored(key: str, in_path: bool):
			return colored(colored("x", colors.fg.red) if in_path else key, *Colors[key])


		res = "Path:\n"
		for y in range(len(self.state.board)):
			for x in range(len(self.state.board[y])):
				res += pretty_colored(self.state.board[y][x],
				               in_path=(x, y) in self.path[1:-1])
			res += "\n"
		return res


