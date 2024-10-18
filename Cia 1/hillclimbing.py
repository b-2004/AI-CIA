
def hill_climbing(graph, start, goal, h):
    current = start
    path = [current]
    while current != goal:
        neighbors = graph[current]
        next_node = min(neighbors, key=lambda x: h[x[0]])[0]
        if h[next_node] >= h[current]:
            return None
        current = next_node
        path.append(current)
    return path
