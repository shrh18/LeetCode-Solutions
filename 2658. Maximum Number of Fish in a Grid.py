class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        direc = [(1,0), (0,1), (-1, 0), (0,-1)]
        R, C = len(grid), len(grid[0])
        visited = [[False for _ in range(C)] for _ in range(R)]
        
        def backtrack(r, c):
            if (r<0 or r>=R) or (c<0 or c>=C) or grid[r][c] == 0 or visited[r][c]:
                return 0
            visited[r][c] = True
            total = grid[r][c]
            for dr, dc in direc:
                
                total += backtrack(r+dr, c+dc)
            return total
        
        maxFishes = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] != 0:
                    maxFishes = max(maxFishes, backtrack(i, j))

        return maxFishes