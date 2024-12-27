class Solution:
    def isHappy(self, n: int) -> bool:

        while n>=1:
            arr = str(n)
            n = 0
            for s in arr:
                n += (int(s))**2
            if n<10:
                if n==1 or n==7:
                    return True
                else:
                    return False

             

        