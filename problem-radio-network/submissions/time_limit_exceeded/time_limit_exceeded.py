import sys

def solve():
    input = sys.stdin.buffer.readline

    n, m, C = map(int, input().split())

    edges = []

    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((w, u - 1, v - 1))

    # Normal sorting
    edges.sort()

    # tree[i] represents which component station i currently belongs to
    tree = list(range(n))

    total = 0
    used = 0

    for w, u, v in edges:
        # If u and v are already in the same component, skip this edge
        if tree[u] == tree[v]:
            continue

        old_tree = tree[v]
        new_tree = tree[u]

        total += w
        used += 1

        # Slow part:
        # scan every station and relabel the whole old component
        for i in range(n):
            if tree[i] == old_tree:
                tree[i] = new_tree

        if used == n - 1:
            print(total)
            return

    print(0 if n == 1 else -1)


if __name__ == "__main__":
    solve()