from collections import OrderedDict

class Graph(object):
	def __init__(self, directed=False):
		self.matrix = OrderedDict()
		self.directed = directed

	def add_point(self, *names):
		for name in names:
			if name not in self.matrix:
				self.matrix[name] = OrderedDict()

	def del_point(self, *names):
		for name in names:
			if name in self.matrix:
				del self.matrix[name]
		for point in self.matrix:
			for name in names:
				if name in self.matrix[point]:
					del self.matrix[point][name]

	def add_edge(self, p1, p2, weight=1):
		self.add_point(p1)
		self.add_point(p2)
		self.matrix[p1][p2] = weight
		if not self.directed:
			self.matrix[p2][p1] = weight

	def _find_edge(self, p1, p2):
		return self.matrix.get(p1, {}).get(p2, None)

	def get_points(self):
		return self.matrix.keys()

	def bfs(self, root):
		visited = [root]
		visited_set = set(visited)
		i = 0
		while i < len(self.matrix.keys()):
			points = [p for p in self.matrix.get(visited[i], {}).keys() if p not in visited]
			visited_set.union(set(points))
			visited.extend(points)
			yield visited[i]
			i += 1
