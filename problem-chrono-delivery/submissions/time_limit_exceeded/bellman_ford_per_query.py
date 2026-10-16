# Correct but too slow: runs Bellman-Ford (Lecture 14) from scratch for every
# request, costing O(N*M) each and O(Q*N*M) overall, instead of computing
# all pairs once as Floyd-Warshall does
import sys


def bellman_ford(n: int, edges: list[tuple[int, int, int]], source: int) -> list[float]:
    """Shortest times from source to every station, O(N*M)"""
    inf = float('inf')
    dist = [inf] * n
    dist[source] = 0

    for _ in range(n - 1):
        changed = False
        for u, v, t in edges:
            if dist[u] != inf and dist[u] + t < dist[v]:
                dist[v] = dist[u] + t
                changed = True
        if not changed:
            break

    return dist


def find_paradoxes(n: int, edges: list[tuple[int, int, int]], dist: list[float]) -> list[bool]:
    """Mark stations affected by a time loop"""
    inf = float('inf')
    bad = [False] * n

    for _ in range(n):
        changed = False
        for u, v, t in edges:
            if dist[u] != inf and not bad[v] and (bad[u] or dist[u] + t < dist[v]):
                bad[v] = True
                changed = True
        if not changed:
            break

    return bad


def answer_queries(n: int, edges: list[tuple[int, int, int]],
                   queries: list[tuple[int, int]]) -> list[str]:
    """Answer each request by running Bellman-Ford from its start station,
    repeats O(N*M) work for every request: O(Q*N*M) overall"""
    out = []
    for a, b in queries:
        dist = bellman_ford(n, edges, a)
        bad = find_paradoxes(n, edges, dist)

        if bad[b]:
            out.append("PARADOX")
        elif dist[b] == float('inf'):
            out.append("UNREACHABLE")
        else:
            out.append(str(dist[b]))
    return out


def main():
    data = sys.stdin.read().split()
    idx = 0
    N, M, Q = int(data[idx]), int(data[idx+1]), int(data[idx+2])
    idx += 3

    edges = []
    for _ in range(M):
        edges.append((int(data[idx]), int(data[idx+1]), int(data[idx+2])))
        idx += 3

    queries = []
    for _ in range(Q):
        queries.append((int(data[idx]), int(data[idx+1])))
        idx += 2

    sys.stdout.write("\n".join(answer_queries(N, edges, queries)) + "\n")


if __name__ == "__main__":
    main() 