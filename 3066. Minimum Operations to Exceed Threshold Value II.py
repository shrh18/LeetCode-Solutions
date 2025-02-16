class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        opCount = 0
        heapq.heapify(nums)

        while True:
            if nums[0]>=k:
                return opCount
            else:
                x = heapq.heappop(nums)
                y = heapq.heappop(nums)
                heapq.heappush(nums, (min(x,y)*2 + max(x,y)))
                opCount += 1