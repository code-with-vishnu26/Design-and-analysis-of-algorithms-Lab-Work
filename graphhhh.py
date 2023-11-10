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


def find_path_from_start(graph, start_node):
    num_nodes = len(graph)
    path = find_path(start_node, [False] * num_nodes, [], start_node)
    return path


graph = {
      0: [1, 2, 3],
    1: [3, 4],
    2: [4, 5, 6],
    3: [5,2],
    4: [6, 2],
    5: [1,3]
}

start_node = 0  
path = find_path_from_start(graph, start_node)

if path:
    print("Path from {} that visits each element once: {}".format(start_node, " -> ".join(map(str, path))))
else:
    print("No path found.")
