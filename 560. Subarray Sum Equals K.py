class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre = 0
        dic = defaultdict(int)
        dic[0] += 1
        count = 0

        for i in range(len(nums)):
            pre += nums[i]
            if pre - k in dic:
                count += dic[pre-k]
            
            dic[pre] += 1

        return count

        
        
