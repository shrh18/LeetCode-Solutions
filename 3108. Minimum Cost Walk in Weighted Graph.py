class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        parent = [i for i in range(n)]
        cost = {}
        ret = []

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

        for u, v, w in edges:
            union(u, v)

        for u, v, w in edges:
            root = find(u)
            if root not in cost:
                cost[root] = w
            else:
                cost[root] &= w

        for src, dest in query:
            r1, r2 = find(src), find(dest)
            if r1 != r2:
                ret.append(-1)
            else:
                ret.append(cost[r1])

        return ret
