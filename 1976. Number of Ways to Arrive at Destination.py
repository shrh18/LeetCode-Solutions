class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        graph = defaultdict(list)

        for src, dest, w in roads:
            graph[src].append((dest, w))
            graph[dest].append((src, w))

        heap = [(0,0)]
        shortest_dist = {i:math.inf for i in range(n)}
        shortest_dist[0] = 0
        ways = {i:0 for i in range(n)}
        ways[0] = 1
        heapq.heapify(heap)

        while heap:
            currDis, curr = heapq.heappop(heap)

            if currDis > shortest_dist[curr]:
                continue
            
            for dest, w in graph[curr]:
                newDis = currDis + w

                if newDis < shortest_dist[dest]:
                    shortest_dist[dest] = newDis
                    ways[dest] = ways[curr]
                    heapq.heappush(heap, (newDis, dest))
                elif newDis == shortest_dist[dest]:
                    ways[dest] += ways[curr]

        return ways[n-1] % MOD