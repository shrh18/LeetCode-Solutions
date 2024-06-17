class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        if n==3:
            return 3
        if n>3:
            counts = [0]*n
            counts[1-1] = 1
            counts[2-1] = 2
            counts[3-1] = 3

            for i in range(4,n+1):
                counts[i-1] = counts[i-1-1] + counts[i-2-1]
        print(counts[-1])
        return counts[-1]
        
                
              