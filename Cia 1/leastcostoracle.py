
import heapq

def least_cost_oracle(graph, start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start, [start]))
    while open_list:
        cost, node, path = heapq.heappop(open_list)
        if node == goal:
            return path
        for neighbor, neighbor_cost in graph[node]:
            heapq.heappush(open_list, (cost + neighbor_cost, neighbor, path + [neighbor]))
    return None
