class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-i for i in piles]
        heapq.heapify(piles)

        for i in range(k):
            st = -heapq.heappop(piles)
            st -= math.floor(st/2)
            heapq.heappush(piles, -st)

        return -sum(piles)
