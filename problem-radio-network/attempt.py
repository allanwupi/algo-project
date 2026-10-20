# Radio Network
# Attempt 1 - Kruskal

class DisjointSets:
    def __init__(self, num_sets: int):
        self.__parent = [i for i in range(num_sets)]
        self.__rank = [0 for _ in range(num_sets)]

    def make_set(self) -> int:
        i = len(self.__parent)
        self.__parent.append(i)
        self.__rank.append(0)
        return i

    def find(self, i: int) -> int:
        # Find the root of i's tree
        root = i
        while self.__parent[root] != root:
            root = self.__parent[root]
        # Make all of i's ancestors children of the root
        curr = i
        while self.__parent[curr] != curr:
            parent = self.__parent[curr]
            self.__parent[curr] = root
            curr = parent
        return root

    def union(self, i: int, j: int):
        i = self.find(i)
        j = self.find(j)
        if i == j: # Nothing to do, already same set
            return
        if self.__rank[i] < self.__rank[j]:
            i, j = j, i
        self.__parent[j] = i
        self.__rank[i] = max(self.__rank[i], self.__rank[j] + 1)


# edge: (u, v, weight)
def kruskals(num_verts: int, edges: list[tuple[int, int, int]]) -> tuple[int, int]:
    sets = DisjointSets(num_verts)
    edges.sort(key=lambda x: x[2])
    total_weight = 0
    num_edges = 0
    for u, v, w in edges:
        if sets.find(u) != sets.find(v):
            total_weight += w
            num_edges += 1
            if num_edges == num_verts - 1:
                return num_edges, total_weight
            sets.union(u, v)
    return num_edges, total_weight

N, M, C = list(map(int, input().split()))
edges = []

for _ in range(M):
    u, v, w = list(map(int, input().split()))
    # Since edges are numbered from 1..N, subtract 1
    edges.append((u-1, v-1, w))

edges_in_tree, min_tree_weight = kruskals(N, edges)
# if there aren't V-1 edges in the resulting 'tree', the tree is actually a forest
answer = min_tree_weight if edges_in_tree == N-1 else -1
print(answer)
