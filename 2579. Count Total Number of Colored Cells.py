class Solution:
    def coloredCells(self, n: int) -> int:

        def totsum(n):
            ss = 0
            for num in range(n-1, 0, -1):
                ss += num
            return ss

        return (2*n-1)**2 - 4*(totsum(n)) 

