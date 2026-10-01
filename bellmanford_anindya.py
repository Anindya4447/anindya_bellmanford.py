def bellman_ford(vertices, edges, source):
    # Initialize distances
    dist = [float('inf')] * vertices
    dist[source] = 0

    # Relax all edges V-1 times
    for _ in range(vertices - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Check for negative weight cycle
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            print("Negative weight cycle detected")
            return

    # Print shortest distances
    print("Vertex \t Distance from Source")
    for i in range(vertices):
        print(i, "\t", dist[i])


# Number of vertices
V = 5

# Edges: (source, destination, weight)
edges = [
    (0, 1, -1),
    (0, 2, 4),
    (1, 2, 3),
    (1, 3, 2),
    (1, 4, 2),
    (3, 2, 5),
    (3, 1, 1),
    (4, 3, -3)
]

# Starting vertex
source = 0

bellman_ford(V, edges, source)
