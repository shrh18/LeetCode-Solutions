class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        lcycle = 0
        l2cycle = []
        visited = [False]*n
        
        for i in range(n):
            if visited[i]: continue
            start, curr = i, i
            currset = set()
            while not visited[curr]:
                visited[curr] = True
                currset.add(curr)
                curr = favorite[curr]
            if curr in currset:
                ll = len(currset)
                while curr != start:
                    ll -= 1
                    start = favorite[start]
                lcycle = max(lcycle, ll)
                if ll == 2:
                    l2cycle.append([curr, favorite[curr]])

        inverted = defaultdict(list)
        for dest, src in enumerate(favorite):
            inverted[src].append(dest)

        def bfs(src, parent):
            q = deque([(src, 0)])
            mm = 0
            while q:
                node, length = q.popleft()
                if node == parent: continue
                mm = max(mm, length)
                for nei in inverted[node]:
                    q.append((nei, length+1))
            return mm

        chainSum = 0
        for n1, n2 in l2cycle:
            chainSum += bfs(n1, n2) + bfs(n2, n1) + 2
        return max(lcycle, chainSum)
