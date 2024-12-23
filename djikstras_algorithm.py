import heapq

def dijkstra(graph, start):
    n = len(graph)
    distances = [float('inf')] * n
    distances[start] = 0
    min_heap = [(0, start)]  # (distance, current_node)

    while min_heap:
        current_distance, current = heapq.heappop(min_heap)

        for neighbor, weight in graph[current]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))

    return distances


# Example Graph (Adjacency List with weights)
graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: [],
}

distances = dijkstra(graph, 0)
print("Shortest Distances from Node 0:", distances)
