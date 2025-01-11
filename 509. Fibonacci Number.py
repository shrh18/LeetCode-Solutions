class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1

        fibs = []
        fibs.append(1)
        fibs.append(1)

        for i in range(3, n+1):
            fibs.append(fibs[-1]+fibs[-2])

        return fibs[-1]
        