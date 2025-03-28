class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:

        direc = [[1,0], [0,1], [-1,0], [0, -1]]
        R, C = len(grid), len(grid[0])

        heap = [(grid[0][0], 0, 0)]
        heapq.heapify(heap)

        visited = set()
        visited.add((0,0))
        sq = sorted(enumerate(queries), key=lambda x:x[1])
        ret = [0]*len(queries)
        count = 0
        
        while heap:
            val, r, c = heapq.heappop(heap)
            
            while sq and sq[0][1] <= val:
                i, j = sq.pop(0)
                ret[i] = count

            count += 1
            for dr, dc in direc:
                if 0 <= r+dr < R and 0 <= c+dc < C and (r+dr,c+dc) not in visited:
                    visited.add((r+dr, c+dc))
                    heapq.heappush( heap, (grid[r+dr][c+dc], r+dr, c+dc))

        for i, j in sq:
            ret[i] = count

        return ret