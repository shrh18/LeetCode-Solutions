class Solution:
    def minOperations(self, n: int) -> int:
        ops = 0
        while n>0:
            p = 0
            i = 0
            while p<n:
                i += 1
                p = pow(2, i)
            if abs(n-p)<abs(n-(pow(2, i-1))):
                n = abs(n-p)
            else:
                n = abs(n-(pow(2, i-1)))
            ops += 1
            print(n)
            
        return ops
                