from ex2 import Node
from ex2.Node import Node_String


class State:

	def __init__(self, start, goal):
		self.start = start
		self.goal = goal


	def get_dist(self, a: str) -> int:
		if a == self.goal:
			return 0
		dist = 0
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
			child = Node_String(val, node, self.get_dist(val))
			node.children.append(child)


