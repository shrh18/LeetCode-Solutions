import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-gg for gg in gifts]
        heapq.heapify(heap)

        while k>0:
            heapq.heappush(heap, -math.floor(math.sqrt(-heapq.heappop(heap))))
            k-=1

        return -sum(heap)