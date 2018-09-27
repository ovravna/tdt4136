

class Node:

	def __init__(self, value, parent, initial_dist: float = 0):

		self.children: [Node] = []
		self.parent: Node = parent
		self.value = value

		if parent:
			self.path = parent.path[:]
			self.path.append(value)
		else:
			self.path = [value]

		self.dist = initial_dist

	def __str__(self):
		return str(self.value)
