from queue import PriorityQueue

from ex2 import State
from ex2.Node import Node
from ex2.State import Board, _Board


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
					if _Board[self.state.board[y][x]] == -1:
						continue

					count += 1
					if not child.dist:
						self.path = child.path
						break
					self.priorityQueue.put((child.dist, count, child))
		if not self.path:
			print("failed...")
		return self.path

	def prittify(self):
		res = ""
		for y in range(len(self.state.board)):
			for x in range(len(self.state.board[y])):
				if (x, y) == self.path[0]:
					res += "A"
				elif (x, y) == self.path[-1]:
					res += "B"
				elif (x, y) in self.path[1:-1]:
					res += "*"
				else:
					res += self.state.board[y][x]
			res += "\n"
		return res
				# elem = self.state.board[y][x]
				# if elem in Board.values():
				# 	if elem == Board['start']:
				# 		pass
				# 	if elem == Board['goal']:
				# 		pass

