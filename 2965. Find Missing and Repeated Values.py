class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        ss = set([i for i in range(1, n**2 + 1)])
        saw = set()
        ans = [None, None]

        for i in range(n):
            for j in range(n):
                if grid[i][j] in saw:
                    ans[0] = grid[i][j]
                else:
                    saw.add(grid[i][j])
                    ss.remove(grid[i][j])

        ans[1] = ss.pop()

        return ans