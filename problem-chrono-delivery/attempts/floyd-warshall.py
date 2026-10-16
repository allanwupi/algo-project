# Chrono Delivery
# Attempt #1 - Floyd-Warshall

N, M, Q = list(map(int, input().split()))


def floyd_warshall(adjmat: list[list[int]], V: int):
    dist: list[list[int]] = [[INFINITY]*N for _ in range(N)]
    for u in range(V):
        for v in range(V):
            dist[u][v] = adjmat[u][v]
    for u in range(V):
        dist[u][u] = 0
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[j][j]
"""
let dist be a |V| x |V| array of minimum distances initialized to ∞ (infinity)
for each edge (u, v) do
    dist[u][v] = w(u, v)  // The weight of the edge (u, v)
for each vertex v do
    dist[v][v] = 0
for k from 1 to |V|
    for i from 1 to |V|
        for j from 1 to |V|
            if dist[i][j] > dist[i][k] + dist[k][j]
                dist[i][j] = dist[i][k] + dist[k][j]
            end if
"""

# Create adjacency matrix (N x N)
INFINITY = 1_000_000
adjmat: list[list[int]] = [[INFINITY]*N for _ in range(N)]
for _ in range(M):
    u, v, t = list(map(int, input().split()))
    if t < adjmat[u][v]:
        adjmat[u][v] = t

requests: list[tuple[int, int]] = []
for _ in range(Q):
    u, v = tuple(map(int, input().split()))
    requests.append((u, v))