import heapq

def prim_mst(graph):
    n = len(graph)  # Number of vertices
    visited = [False] * n
    mst = []  # Edges in the MST
    min_heap = [(0, 0, -1)]  # (weight, current_node, previous_node)

    while min_heap:
        weight, current, previous = heapq.heappop(min_heap)
        if visited[current]:
            continue
        visited[current] = True
        if previous != -1:
            mst.append((previous, current, weight))

        for neighbor, edge_weight in graph[current]:
            if not visited[neighbor]:
                heapq.heappush(min_heap, (edge_weight, neighbor, current))

    return mst


# Example Graph (Adjacency List with weights)
graph = {
    0: [(1, 1), (2, 2)],
    1: [(0, 1), (2, 2), (3, 3)],
    2: [(0, 2), (1, 2), (3, 4)],
    3: [(1, 3), (2, 4)],
}

mst = prim_mst(graph)
print("Minimum Spanning Tree:", mst)
