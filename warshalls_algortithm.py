def warshall(graph):
    n = len(graph)
    reach = [[0] * n for _ in range(n)]

    # Initialize the reachability matrix based on adjacency matrix
    for i in range(n):
        for j in range(n):
            reach[i][j] = graph[i][j]

    # Update reachability using Warshall's Algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])

    return reach


# Example Graph (Adjacency Matrix)
graph = [
    [0, 1, 0],
    [0, 0, 1],
    [0, 0, 0],
]

reachability = warshall(graph)
print("Reachability Matrix:")
for row in reachability:
    print(row)
