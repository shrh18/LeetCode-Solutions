class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        
        diff, high, ans = 0, 0, 0

        for num in nums:
            ans = max(ans, diff*num)
            diff = max(high-num, diff)
            high = max(high, num)

        return ans

        