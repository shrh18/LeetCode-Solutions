class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ret = set()
        seen = set()
        l, r = 0, 9

        while r < len(s):
            if s[l:r+1] in seen:
                ret.add(s[l:r+1])
            seen.add(s[l:r+1])
            l += 1
            r += 1

        return list(ret)
                