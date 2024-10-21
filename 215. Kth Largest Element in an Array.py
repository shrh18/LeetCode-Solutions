class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return None
        heapq.heapify(nums)
        ret = 0
        for j in range(len(nums)-k+1):
            ret = heapq.heappop(nums)
        return ret