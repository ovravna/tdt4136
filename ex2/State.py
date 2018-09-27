from ex2 import Node


class State(object):

	def __init__(self, value, parent: Node, start: Node, goal: Node):


		self.childern: [Node] = []
		self.parent = parent
		self.value = value
		self.dist: int = 0


		if parent:
			self.path = parent.path[:]
			self.path.append(value)
			self.start = parent.start
			self.goal = parent.goal

		else:
			self.path = [value]
			self.start = start
			self.goal = goal


class State_String(State):

	def __init__(self, value: str, parent: Node, start: Node, goal: Node+):



