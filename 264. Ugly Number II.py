class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        seen = set([1])
        heap = [1]
        heapq.heapify(heap)

        for i in range(n):
            x = heapq.heappop(heap)
            for fac in [2,3,5]:
                u = x*fac
                if u not in seen:
                    seen.add(u)
                    heapq.heappush(heap, u)

        return x
