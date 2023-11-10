def shortest_path(n, m, edges, demons):
    pq = [(0, 1)]  
    visited = set()
    while pq:
        pq.sort()
        time, node = pq.pop(0)
        if (time, node) in visited:
            continue
        visited.add((time, node))
        if node == n:
            return time
        for start, end, weight in edges:
            if start == node:
                new_time = time + weight
                while new_time in demons[end]:
                    new_time += 1  
                pq.append((new_time, end))

n, m = map(int, input().split())
edges = []
for _ in range(m):
    edge = tuple(map(int, input().split()))
    edges.append(edge)
demons = {}
for node in range(1, n+1):
    jam_times = list(map(int, input().split()[1:]))
    demons[node] = jam_times

result = shortest_path(n, m, edges, demons)
print(result)
