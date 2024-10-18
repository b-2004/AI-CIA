
import heapq

def astar(graph, start, goal, h):
    open_list = []
    heapq.heappush(open_list, (h[start], start))
    path = {}
    g_score = {start: 0}

    while open_list:
        current = heapq.heappop(open_list)[1]
        if current == goal:
            result = []
            while current:
                result.append(current)
                current = path.get(current)
            return result[::-1]

        for neighbor, cost in graph[current]:
            new_g = g_score[current] + cost
            if new_g < g_score.get(neighbor, float('inf')):
                path[neighbor] = current
                g_score[neighbor] = new_g
                f_score = new_g + h[neighbor]
                heapq.heappush(open_list, (f_score, neighbor))
    return None
