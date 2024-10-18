
def aostar(graph, start, goal):
    visited = []
    def recursive_search(node):
        if node in goal:
            return True
        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                if recursive_search(neighbor):
                    return True
        return False

    recursive_search(start)
    return visited[::-1]
