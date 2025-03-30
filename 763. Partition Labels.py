class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {}

        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]][1] = i
            else:
                dic[s[i]] = [i,i]

        vals = sorted(list(dic.values()))

        i = 1
        while i < len(vals):
            if vals[i-1][1] > vals[i][0]:
                if vals[i-1][1] > vals[i][1]:
                    vals[i] = [vals[i-1][0], vals[i-1][1]]
                else:
                    vals[i] = [vals[i-1][0], vals[i][1]]
                
                del vals[i-1]
            else:
                i += 1

        for i in range(len(vals)):
            vals[i] = vals[i][1] - vals[i][0] + 1

        return vals