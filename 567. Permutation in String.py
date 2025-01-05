class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1c = {letter:0 for letter in ascii_lowercase}
        s2c = {letter:0 for letter in ascii_lowercase}
        
        for i in range(len(s1)):
            s1c[s1[i]] += 1

        l = 0
        r = l + len(s1) - 1
        for i in range(l, r+1):
            s2c[s2[i]] += 1

        while r < len(s2):
            if s2c == s1c:
                return True
            s2c[s2[l]] -= 1
            l += 1
            r += 1
            if r<len(s2):
                s2c[s2[r]] += 1 
            
        return False
