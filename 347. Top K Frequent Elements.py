class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        eachFreq = {}
        for num in nums:
            if num in eachFreq:
                eachFreq[num]+=1
            else:
                eachFreq[num] = 1

        newL = dict(sorted(eachFreq.items(), key = lambda x: x[1], reverse=True))
        return list(newL.keys())[:k]
        