class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for idx, val in enumerate(arr):
            heapq.heappush(heap, (abs(val-x), idx))
        
        ret = []
        while k>0:
            (dif, idx) = heapq.heappop(heap)
            ret.append(arr[idx])
            k-=1
        return sorted(ret)

        