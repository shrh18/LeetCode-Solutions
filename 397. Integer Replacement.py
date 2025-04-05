class Solution:
    def integerReplacement(self, n: int) -> int:
        
        op = 0
        while n != 1:

            if n == 2:
                return op+1
            if n == 3:
                return op+2

            if n%2 == 0:
                n = n//2
            else:
                if (n-1)%4 == 0:
                    n = n-1
                else:
                    n = n+1
            op += 1

        return op