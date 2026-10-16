# Intended solution: Floyd-Warshall in O(N^3 + Q). The inner j loop is a single row
# update (list comprehension), which cuts Python's per-step overhead versus a plain loop
import sys


def floyd_warshall(d: list[list[float]]) -> list[list[float]]:
    """Floyd-Warshall (Lecture 15): for each stopover k, keep the faster of
    the best route i -> j so far and the route i -> k -> j. O(n^3) time""" 
    n = len(d)
    for k in range(n):
        dk = d[k]
        for i in range(n):
            row = d[i]
            dik = row[k]
            if dik == float('inf'):
                continue
            # Third (j) loop condensed into a list comprehension:
            d[i] = [a if a <= dik + b else dik + b for a, b in zip(row, dk)]
    return d


def find_paradoxes(d: list[list[float]]) -> list[bytearray]:
    """Mark (i, j) as a paradox if i can reach a station k on a time loop
    and k can reach j, so the courier could lap the loop forever"""
    n = len(d)
    inf = float('inf')
    paradox = [bytearray(n) for _ in range(n)]

    for k in range(n):
        if d[k][k] < 0:
            out_k = [j for j in range(n) if d[k][j] != inf]
            for i in range(n):
                if d[i][k] != inf:
                    pi = paradox[i]
                    for j in out_k:
                        pi[j] = 1

    return paradox


def main():
    data = sys.stdin.read().split()
    idx = 0
    N, M, Q = int(data[idx]), int(data[idx+1]), int(data[idx+2])
    idx += 3

    # Distance table: inf = no route known, 0 from each station to itself
    inf = float('inf')
    d = [[inf] * N for _ in range(N)]
    for i in range(N):
        d[i][i] = 0


    # Read wormholes and fill into distance table
    for _ in range(M):
        u, v, t = int(data[idx]), int(data[idx+1]), int(data[idx+2])
        idx += 3
        if t < d[u][v]:
            d[u][v] = t

    d = floyd_warshall(d)
    paradox = find_paradoxes(d)

    # Read delivery requests
    out = []
    for _ in range(Q):
        a, b = int(data[idx]), int(data[idx+1])
        idx += 2
        if paradox[a][b]:
            out.append("PARADOX")
        elif d[a][b] == inf:
            out.append("UNREACHABLE")
        else:
            out.append(str(d[a][b]))

    sys.stdout.write("\n".join(out) + "\n")  # single write is faster than many prints


if __name__ == "__main__":
    main()