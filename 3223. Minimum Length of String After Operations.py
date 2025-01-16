class Solution:
    def minimumLength(self, s: str) -> int:
        dic = defaultdict(int)
        i = 0
        val = 0
        while i < len(s):
            dic[s[i]] += 1
            if dic[s[i]] == 3:
                dic[s[i]] -= 2
            i += 1

        for k, v in dic.items():
            val += v
        return val

