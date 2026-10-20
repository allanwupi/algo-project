import sys

def solve():
    input = sys.stdin.buffer.readline

    n, m, C = map(int, input().split())

    # Counting sort idea:
    # store edges in buckets according to their construction cost
    buckets = [[] for _ in range(C + 1)]

    for _ in range(m):
        u, v, w = map(int, input().split())
        buckets[w].append((u - 1, v - 1))

    # Disjoint Set / Union-Find
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        # Find the representative of x's component
        # Path compression keeps future find operations fast
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        a = find(a)
        b = find(b)

        # Already connected, so adding this edge would create a cycle
        if a == b:
            return False

        # Union by rank
        if rank[a] < rank[b]:
            a, b = b, a

        parent[b] = a

        if rank[a] == rank[b]:
            rank[a] += 1

        return True

    total = 0
    used = 0

    # Process edges from smallest cost to largest cost
    # This replaces the normal sorting step in Kruskal's algorithm
    for w in range(1, C + 1):
        for u, v in buckets[w]:

            # Add the edge only if it connects two different components
            if union(u, v):
                total += w
                used += 1

                # A spanning tree with n vertices has exactly n - 1 edges
                if used == n - 1:
                    print(total)
                    return

    print(0 if n == 1 else -1)


if __name__ == "__main__":
    solve()