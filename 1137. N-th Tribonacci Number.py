class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1

        ret = [0]*(n+1)
        ret[0], ret[1], ret[2] = 0, 1, 1
        for i in range(3, n+1):
            ret[i] = ret[i-1] + ret[i-2] + ret[i-3]

        return ret[-1]

        