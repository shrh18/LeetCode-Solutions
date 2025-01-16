class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs[0]) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        strs.sort()
        ret = ""

        for i in range(len(strs[0])):
            if strs[0][i] == strs[-1][i]:
                ret += strs[0][i]
            else:
                return ret

        return ret