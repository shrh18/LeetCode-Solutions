class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nn = set()
        for i in nums:
            if i in nn:
                return i
            else:
                nn.add(i)
        