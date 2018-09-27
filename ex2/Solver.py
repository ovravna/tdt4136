from queue import PriorityQueue
from typing import Optional

from ex2 import State
from ex2.Node import Node_String, Node


class Solver:

	def __init__(self, initial_node: Node, state: State):
		self.state: State = state
		self.path = []
		self.visitQueue = []
		self.priorityQueue = PriorityQueue()
		self.node: Node = initial_node

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
					count += 1
					if not child.dist:
						self.path = child.path
						break
					self.priorityQueue.put((child.dist, count, child))
		if not self.path:
			print("failed...")
		return self.path

