class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        direc = [(1,0), (0,1), (-1,0), (0,-1)]
        R, C = len(grid), len(grid[0])
        islandId, maxSize = 2, 0
        islandSizes = {}
    
        def dfs(x, y, islandId):
            if x<0 or x>=R or y<0 or y>=C or grid[x][y]!=1:
                return 0
            grid[x][y] = islandId
            size = 1
            for dx, dy in direc:
                size += dfs(x+dx, y+dy, islandId)
            return size

        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    islandSizes[islandId] = dfs(i, j, islandId)
                    maxSize = max(maxSize, islandSizes[islandId])
                    islandId += 1

        for i in range(R):
            for j in range(C):
                if grid[i][j] == 0:
                    neiIs = set()
                    for dx, dy in direc:
                        x, y = i+dx, j+dy
                        if 0<=x<C and 0<=y<R and grid[x][y] != 0:
                            neiIs.add(grid[x][y])
                    currSize = 1 + sum(islandSizes[island] for island in neiIs)
                    maxSize = max(maxSize, currSize)

        return maxSize