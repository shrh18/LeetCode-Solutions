class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        low, high = 0, len(s)
        ret = []
        if s[0] == 'I':
            ret.append(low)
            low += 1
        else:
            ret.append(high)
            high -= 1 
        
        for i in range(1, len(s)):
            if s[i] == 'I':
                ret.append(low)
                low += 1
            else:
                ret.append(high)
                high -= 1

        ret.append(high)
        return ret

