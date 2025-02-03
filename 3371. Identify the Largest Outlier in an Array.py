class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        ss = sum(nums)
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1
        
        ret = set()
        numSet = set(nums)
        
        for num in nums:
            freq[num] -= 1
            if (ss - num) % 2 == 0:
                target = (ss-num)//2
                if target == num:
                    if target in numSet and freq[num]:
                        ret.add(num)
                elif target in numSet:
                        ret.add(num)
            freq[num] += 1
        
        print(ret)
        return max(ret)