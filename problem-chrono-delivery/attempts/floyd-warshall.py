# Chrono Delivery
# Attempt #1 - Floyd-Warshall

from pprint import pprint

INFINITY = 1_000_000

N, M, Q = list(map(int, input().split()))

"""FLOYD WARSHALL PSEUDOCODE
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

def floyd_warshall(adjmat: list[list[int]]):
    dist: list[list[int]] = [[INFINITY]*N for _ in range(N)]
    V = len(dist)
    for u in range(V):
        for v in range(V):
            dist[u][v] = adjmat[u][v]
    for u in range(V):
        dist[u][u] = 0
    pprint(dist)
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[j][j]
    pprint(dist)
    # Find negative cycles
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = -INFINITY
    pprint(dist)
    return dist

def request(dist: list[list[int]], u: int, v: int):
    length = dist[u][v]
    V = len(dist)
    if length == -INFINITY:
        return "PARADOX"
    if length == INFINITY:
        return "UNREACHABLE"
    return length

# Create adjacency matrix (N x N)
adjmat: list[list[int]] = [[INFINITY]*N for _ in range(N)]
for _ in range(M):
    u, v, t = list(map(int, input().split()))
    if t < adjmat[u][v]:
        adjmat[u][v] = t

all_shortest_paths = floyd_warshall(adjmat)

for _ in range(Q):
    u, v = tuple(map(int, input().split()))
    print(request(all_shortest_paths, u, v))
