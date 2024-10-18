
import heapq

def branch_and_bound_extended(graph, start, goal):
    open_list = []
    visited = set()
    heapq.heappush(open_list, (0, start, [start]))

    while open_list:
        cost, node, path = heapq.heappop(open_list)
        if node in visited:
            continue
        visited.add(node)
        if node == goal:
            return path
        for neighbor, neighbor_cost in graph[node]:
            heapq.heappush(open_list, (cost + neighbor_cost, neighbor, path + [neighbor]))
    return None
