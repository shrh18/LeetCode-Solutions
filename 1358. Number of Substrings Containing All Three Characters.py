class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        dic = defaultdict(int)
        count = 0
        n = len(s)
        l, r = 0, 0

        while r<n:

            dic[s[r]] += 1
            
            while dic['a']>=1 and dic['b']>=1 and dic['c']>=1:
                count += n-r    
                dic[s[l]] -= 1
                l += 1

            r += 1
            
        return count
