class Node:
    def __init__(self, value):
        self.value = value
        self.outbound = []

    def point_to(self, other):
        self.outbound.append(other)


class Graph:
    def __init__(self, root):
        self._root = root

    def dfs(self):
        visited = []
        stack = [self._root]

        while stack:
            vertex = stack.pop()

            if vertex not in visited:
                visited.append(vertex)
                for neighbor in vertex.outbound:
                    stack.append(neighbor)

        return visited


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')

a.point_to(b)
b.point_to(c)
c.point_to(d)
d.point_to(a)
b.point_to(d)

g = Graph(a)
dfs_result = g.dfs()

print(f"Результат: {[node.value for node in dfs_result]}")
