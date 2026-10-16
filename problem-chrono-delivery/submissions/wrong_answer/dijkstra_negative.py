# Incorrect: runs Dijkstra's algorithm (Lecture 14) from each start station
# Negative wormholes are ignored, so it does not calculate the fastest route
# Consequentially, it will never process a time loop, so PARADOX is ignored
import sys
import heapq


def build_adjlist(n: int, edges: list[tuple[int, int, int]]) -> list[list[tuple[int, int]]]:
    """Convert the wormhole list into an adjacency list"""
    adjlist = [[] for _ in range(n)]
    for u, v, t in edges:
        adjlist[u].append((v, t))
    return adjlist


def dijkstra(adjlist: list[list[tuple[int, int]]], source: int) -> list[int | None]:
    """Adapted Dijkstra's from Lecture 14, slide 15"""
    dist = [None] * len(adjlist)
    pq = [(0, source)]

    while pq:
        dd, u = heapq.heappop(pq)
        if dist[u] is not None:
            continue
        dist[u] = dd
        for v, w in adjlist[u]:
            if dist[v] is None:
                heapq.heappush(pq, (dd + w, v))

    return dist


def answer_queries(adjlist: list[list[tuple[int, int]]],
                   queries: list[tuple[int, int]]) -> list[str]:
    """Answer each request from Dijkstra's results. Never outputs PARADOX,
    since Dijkstra's cannot detect time loops"""
    cache = {}
    out = []
    for a, b in queries:
        if a not in cache:
            cache[a] = dijkstra(adjlist, a)
        x = cache[a][b]
        out.append("UNREACHABLE" if x is None else str(x))
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

    adjlist = build_adjlist(N, edges)

    sys.stdout.write("\n".join(answer_queries(adjlist, queries)) + "\n")


if __name__ == "__main__":
    main()