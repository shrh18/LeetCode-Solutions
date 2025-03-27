class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        n = len(nums)
        x = nums[0]
        ret = math.inf

        while r < n:
            # print(f"arr:{nums[l:r+1]}, x:{x}")
            if x >= target:
                ret = min(ret, r+1-l)
                while x >= target and l<n:
                    x -= nums[l]
                    l += 1
                    if x >= target:
                        ret = min(ret, r+1-l)
            elif x < target:
                r += 1
                if r < n:
                    x += nums[r]
            

        return ret if ret is not math.inf else 0

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        n = len(nums)
        x = nums[0]
        ret = math.inf

        while r < n:
            # print(f"arr:{nums[l:r+1]}, x:{x}")
            if x >= target:
                ret = min(ret, r+1-l)
                while x >= target and l<n:
                    x -= nums[l]
                    l += 1
                    if x >= target:
                        ret = min(ret, r+1-l)
            elif x < target:
                r += 1
                if r < n:
                    x += nums[r]
            

        return ret if ret is not math.inf else 0

