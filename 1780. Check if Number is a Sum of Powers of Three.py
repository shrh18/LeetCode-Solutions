class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        ss = set()

        while n>0:
            i = 0
            while pow(3, i) <= n:
                i += 1
            if i-1 in ss:
                return False
            else:
                n -= pow(3, i-1)
                ss.add(i-1)
 
        if n == 0:
            return True
        else:
            return False

        # while n!=0:
        #     r = n%3
        #     if r==2:
        #         return False
        #     n = n//3

        # return True