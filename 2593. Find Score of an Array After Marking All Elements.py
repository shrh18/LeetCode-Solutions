class Solution:
    def findScore(self, nums: List[int]) -> int:
        score = 0
        n = len(nums)
        heap = []
        for idx, val in enumerate(nums):
            heapq.heappush(heap, (val, idx))

        ss = set()
        counter = n
        while counter>0:
            v, i = heapq.heappop(heap)
            if i not in ss:
                score += v
                ss.add(i)
                counter-=1
                if i-1>=0:
                    if i-1 not in ss:
                        counter-=1
                    ss.add(i-1)
                if i+1<n:
                    if i+1 not in ss:
                        counter-=1
                    ss.add(i+1)
        return score