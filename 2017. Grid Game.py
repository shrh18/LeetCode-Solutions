class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        pre = [grid[0][0]]*n
        post = [grid[1][-1]]*n

        for i in range(1, n):
            pre[i] = pre[i-1] + grid[0][i]
            post[-1-i] = post[-i] + grid[1][-1-i]
        print(pre)
        print(post)
        ret = math.inf
        for i in range(n):
            p2 = max(pre[-1]-pre[i], post[0]-post[i])
            ret = min(ret, p2)
        return ret