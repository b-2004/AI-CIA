
import heapq

def best_first_search(graph, start, goal, h):
    open_list = []
    heapq.heappush(open_list, (h[start], start, [start]))

    while open_list:
        _, node, path = heapq.heappop(open_list)
        if node == goal:
            return path
        for neighbor, cost in graph[node]:
            heapq.heappush(open_list, (h[neighbor], neighbor, path + [neighbor]))
    return None
