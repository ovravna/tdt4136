from queue import PriorityQueue

from ex2.Node import Node_String, Node


class Solver:

	def __init__(self, initial_node: Node):
		self.path = []
		self.visitQueue = []
		self.priorityQueue = PriorityQueue()
		# self.start = start
		# self.goal = goal
		self.state: Node = initial_node

	def solve(self):

		state: Node = self.state
		count: int = 0
		self.priorityQueue.put((0, count, state))

		while not self.path and self.priorityQueue.qsize():
			closestChild: Node = self.priorityQueue.get()[2]
			closestChild.create_children()
			self.visitQueue.append(closestChild.value)

			child: Node
			for child in closestChild.children:
				if child.value not in self.visitQueue:
					count += 1
					if not child.dist:
						self.path = child.path
						break
					self.priorityQueue.put((child.dist, count, child))
		if not self.path:
			print("failed...")
		return self.path

