class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        primes = [True]*(right+1)
        primes[0], primes[1] = False, False

        for i in range(2, right+1):
            if primes[i]:
                for j in range(i*i, right+1, i):
                    primes[j] = False
        
        primes = [i for i in range(left, right+1) if primes[i]]

        if len(primes) < 2:
            return [-1, -1]

        minDif = math.inf
        ret = [-1,-1]
        for i in range(1, len(primes)):
            if primes[i]-primes[i-1] < minDif:
                minDif = primes[i]-primes[i-1]
                ret = [primes[i-1], primes[i]]

        return ret

        