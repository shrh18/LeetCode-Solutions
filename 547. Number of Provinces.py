class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = [i for i in range(n)]

        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]

        def union(u, v):
            rootU = find(u)
            rootV = find(v)

            if rootU == rootV:
                return False
            parent[rootV] = rootU
            return True

        edges = []
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    union(i, j)

        uniqueRoots = set()
        for i in range(n):
            uniqueRoots.add(find(i))

        return len(set(uniqueRoots))