class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        seen = set([1])
        heap = [1]
        heapq.heapify(heap)

        for _ in range(n):
            x = heapq.heappop(heap)
            for fac in primes:
                u = fac*x
                if u not in seen:
                    seen.add(u)
                    heapq.heappush(heap, u)

        return x