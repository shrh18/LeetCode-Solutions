class Solution:
    def check(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if nums[i]<nums[i-1]:
                s = []
                s.extend(nums[i:])
                s.extend(nums[:i])
                for j in range(1, len(s)):
                    if s[j]<s[j-1]:
                        return False
                return True

        return True
