class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxCount = 0
        dic = defaultdict(int)
        l = 0
        maxlen = 0
        for r in range(len(s)):
            dic[s[r]] += 1
            maxCount = max(maxCount, dic[s[r]])
            
            while (r-l+1) - maxCount > k:
                dic[s[l]] -= 1
                l += 1
        
            maxlen = max(maxlen, r-l+1)
        return maxlen
