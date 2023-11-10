def find_path(node, visited, path, start):
    visited[node] = True
    path.append(node)
    if len(path) == len(graph):
        if start in graph[node]:
            path.append(start)
            return path
    for neighbor in graph[node]:
        if not visited[neighbor]:
            result = find_path(neighbor, visited, path, start)
            if result:
                return result
    visited[node] = False
    path.pop()
    return None

graph = {
    0: [1, 2],
    1: [2, 3,],
    2: [3, 4],
    3: [4,5],
    4: [5, 2],
    5: [5,6],
    6: [2,6],
    7: [1,3]
}

path = find_path(0, [False] * len(graph), [], 1)
if path:
    print("Path:", " -> ".join(map(str, path)))
else:
    print("No path found.")
