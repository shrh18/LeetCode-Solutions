class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dic = defaultdict(list)
        ret = -1

        for num in nums:
            n = list(str(num))
            n = [int(x) for x in n]
            ss = sum(n)
            dic[ss].append(num)

        for k,v in dic.items():
            if len(v)>1:
                v = sorted(v)
                ret = max(ret, v[-1]+v[-2])
                
        return ret

