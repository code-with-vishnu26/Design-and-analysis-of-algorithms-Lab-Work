class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def count_cycles(self, v, visited, parent):
        visited[v] = True
        cycle_count = 0

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                cycle_count += self.count_cycles(neighbor, visited, v)
            elif parent != neighbor:
                cycle_count += 1

        return cycle_count

    def find_cycles(self):
        visited = [False] * self.vertices
        cycle_count = 0

        for vertex in range(self.vertices):
            if not visited[vertex]:
                cycle_count += self.count_cycles(vertex, visited, -1) // 2

        return cycle_count

g = Graph(5)
g.add_edge(4, 1)
g.add_edge(1, 2)
g.add_edge(2, 4)
g.add_edge(4, 3)
g.add_edge(3, 2)

cycle_count = g.find_cycles()
print("Number of cycles in the graph:", cycle_count)
