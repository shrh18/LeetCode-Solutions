class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        n = len(s)

        if s == "":
            return True
        
        for j in range(len(t)):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1

            if i == n:
                return True

        return False

        