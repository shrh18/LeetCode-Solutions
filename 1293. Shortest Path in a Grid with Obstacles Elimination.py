class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        direc = [(1,0), (0,1), (-1,0), (0,-1)]
        R, C = len(grid), len(grid[0])
        
        def backtrack(x, y, k, visited, cost):
            if y==R-1 and x==C-1:
                self.minCost = min(self.minCost, cost)
                return None
            if cost > self.minCost:
                return
            if (x,y,k) in visited and visited[(x,y,k)] <= cost:
                return 

            visited[(x,y,k)] = cost

            for dx, dy in direc:
                if 0<=x+dx<C and 0<=y+dy<R and (x+dx, y+dy) not in visited:
                    if grid[y+dy][x+dx] == 0:
                        backtrack(x+dx, y+dy, k, visited, cost+1)
                    elif grid[y+dy][x+dx] == 1 and k>0:
                        backtrack(x+dx, y+dy, k-1, visited, cost+1)

        visited = {}
        self.minCost = math.inf
        if grid[0][0] == 1:
            if k == 0:
                return -1
            k -= 1
        backtrack(0, 0, k, visited, 0)

        return self.minCost if self.minCost != math.inf else -1

