
def beam_search(graph, start, goal, width):
    queue = [(start, [start])]
    while queue:
        next_queue = []
        for node, path in queue:
            if node == goal:
                return path
            for neighbor in graph[node]:
                next_queue.append((neighbor, path + [neighbor]))
        queue = sorted(next_queue, key=lambda x: len(x[1]))[:width]
    return None
