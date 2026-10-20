# Race to the Beginning
# Attempt #1 - Bellman-Ford

INFINITY = float('inf')


def bellman_ford_negative_cycle(num_verts: int, edges: list[tuple[int, int, int]], source: int = 0):
    dist: list = [None for _ in range(num_verts)]
    pred: list = [None for _ in range(num_verts)]
    dist[source] = 0
    for _ in range(num_verts-1):
        for u, v, w in edges:
            if dist[u] == None:
                continue
            if dist[v] == None or dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                pred[v] = u
    # Check for negative cycles
    for u, v, w in edges:
        if dist[u] == None:
            continue
        if dist[u] + w < dist[v]:
            return "YES"
    return "NO"


N, M = list(map(int, input().split()))

edges = []
for _ in range(M):
    u, v, t = list(map(int, input().split()))
    edges.append((u, v, t))

print(bellman_ford_negative_cycle(N, edges))
