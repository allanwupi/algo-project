import sys

def solve():
    input = sys.stdin.buffer.readline
    n, m, C = map(int, input().split())

    best = [float("inf")] * n

    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1

        # Wrong idea:
        # each station only keeps its cheapest incident edge
        best[u] = min(best[u], w)
        best[v] = min(best[v], w)

    # If a station has no possible link
    if any(x == float("inf") for x in best):
        print(-1)
        return

    # Wrong: adding each station's cheapest edge does not form an MST
    print(sum(best) // 2)


if __name__ == "__main__":
    solve()