class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        adj = defaultdict(list)
        for src, dest in edges:
            adj[src].append(dest)
            adj[dest].append(src)

        path = []
        bobPath = [-1]*len(amount)

        def traverseBob(node, parent):
            if node == 0:
                return True
            for nei in adj[node]:
                if nei != parent:
                    path.append(node)
                    if traverseBob(nei, node):
                        return True
                    path.pop()

        def getAliceScore(node, parent, currScore, t):
            if bobPath[node] == -1 or bobPath[node] > t:
                currScore += amount[node]
            elif bobPath[node] == t:
                currScore += amount[node] // 2

            if len(adj[node]) == 1 and node != 0:
                return currScore
            else:
                rr = -math.inf
                for nei in adj[node]:
                    if nei != parent:
                        rr = max(rr, getAliceScore(nei, node, currScore, t+1))
                return rr

        traverseBob(bob, -1)
        for i, node in enumerate(path):
            bobPath[node] = i

        traverseBob(bob, -1)
        return getAliceScore(0, -1, 0, 0)