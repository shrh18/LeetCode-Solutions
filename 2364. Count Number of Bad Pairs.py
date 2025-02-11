class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        freq = Counter(nums)
        ids = defaultdict(set) # sub to idx
        count = 0
        rep = 0
        for i in range(len(nums)):
            ids[nums[i]-i].add(i)
        
        for v in freq.values():
            rep += v if v>1 else 0

        total = math.factorial(len(nums))//(math.factorial(len(nums)-2)*2)

        for k,v in ids.items():
            if len(v)>1:
                count += math.factorial(len(v))//(math.factorial(len(v)-2)*2)

        return total-count