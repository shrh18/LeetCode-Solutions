class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]

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

        for u,v in edges:
            if not union(u,v):
                return [u, v]

        return []
