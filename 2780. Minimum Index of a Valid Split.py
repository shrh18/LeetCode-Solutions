class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        dom, fr = 0, -math.inf
        n = len(nums)

        for num in nums:
            freq[num] += 1
            if freq[num] > fr:
                dom = num
                fr = freq[num]

        c1, c2 = 0, 0
        for i in range(n):
            if nums[i] == dom:
                c1 += 1
                c2 = fr - c1

                if c1*2 > i+1 and c2*2 > n-1-i:
                    return i

        return -1