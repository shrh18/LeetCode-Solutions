class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 0
    
        prime = [True]*(n)
        p = 2

        while(p*p <= n):
            if prime[p]:
                for i in range(p*p, n, p):
                    prime[i] = False
            p += 1

        count = 0
        for num in range(2, n):
            if prime[num]:
                count += 1

        return count

