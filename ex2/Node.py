from typing import Optional


class Node(object):

	def __init__(self, value, parent, initial_dist: int = 0):



		self.children: [Node] = []
		self.parent: Node = parent
		self.value = value

		if parent:
			self.path = parent.path[:]
			self.path.append(value)
		else:
			self.path = [value]

		self.dist = initial_dist

	# def get_dist(self) -> int:
	# 	return 0
	# def create_children(self):
	# 	pass



class Node_String(Node):

	def __init__(self, value: str, parent: Optional[Node], initial_dist: int = 0):
		super(Node_String, self).__init__(value, parent, initial_dist)

	# def get_dist(self):
	# 	if self.value == self.goal:
	# 		return 0
	# 	dist = 0
	# 	for i in range(len(self.goal)):
	# 		letter = self.goal[i]
	# 		dist += abs(i - self.value.index(letter))
	# 	return dist
	#
	# def create_children(self):
	# 	if self.children:
	# 		return
	# 	for i in range(len(self.goal) - 1):
	# 		val = self.value
	# 		val = val[:i] + val[i+1] + val[i] + val[i + 2:]
	# 		child = Node_String(val, self, None, None)
	# 		self.children.append(child)

			
