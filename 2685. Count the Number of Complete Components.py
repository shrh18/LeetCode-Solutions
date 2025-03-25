class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
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

        parent = [i for i in range(n)]

        for u, v in edges:
            union(u, v)

        nic = defaultdict(int)
        eic = defaultdict(int)

        for node in range(n):
            root = find(node)
            nic[root] += 1

        for u,v in edges:
            root = find(u)
            eic[root] += 1

        count = 0
        for comp, nodes in nic.items():
            reqEdges = (nodes*(nodes-1)) // 2
            if eic[comp] == reqEdges:
                count += 1

        return count
        