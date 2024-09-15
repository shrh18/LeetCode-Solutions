class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums)%k != 0:
            return False
    
        target = sum(nums)/k
        used = [False]*len(nums)
        cache = {}

        def backtrack(i, k, subSetSum):
            if k==0:
                return True
            if subSetSum == target:
                return backtrack(0, k-1, 0)
            
            state = tuple(used)
            if state in cache:
                return cache[state]

            for j in range(i, len(nums)):
                if used[j] or subSetSum+nums[j]>target or (j>0 and nums[j]==nums[j-1] and not used[j-1]):
                    continue
                used[j] = True
                
                if backtrack(j+1, k, subSetSum+nums[j]):
                    cache[state] = True
                    return True

                used[j] = False
            
            cache[state] = False
            return False

        nums.sort(reverse=True)
        return backtrack(0, k, 0)

        
        