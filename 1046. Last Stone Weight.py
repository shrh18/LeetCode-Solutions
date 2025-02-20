class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)

        while len(stones)>1:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)

            rem = abs(s1-s2)
            if rem>0:
                heapq.heappush(stones, -rem)

        return -heapq.heappop(stones) if len(stones)>0 else 0
