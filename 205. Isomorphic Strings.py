class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        dic[s[0]] = t[0]
        ss =set()
        ss.add(t[0])

        for i in range(1, len(s)):
            if s[i] in dic:
                if dic[s[i]] != t[i]:
                    return False
            else:
                if t[i] in ss:
                    return False
                dic[s[i]] = t[i]
                ss.add(t[i])

        return True

