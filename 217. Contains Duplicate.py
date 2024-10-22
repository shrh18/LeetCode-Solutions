class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        gg = set()
        for num in nums:
            if num in gg:
                return True
            else:
                gg.add(num)
        return False