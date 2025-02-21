class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        t = [i%24 for i in hours]
        seen = set()
        dic = defaultdict(list)
        for i in range(len(t)):
            dic[t[i]].append(hours[i])
        count = 0
        print(dic)
        for i in range(len(t)):
            if t[i] == 0:
                diff = 0
            else:
                diff = 24-t[i]
            if diff not in seen:
                if diff == t[i]:
                    if len(dic[diff])>1:
                        count += comb(len(dic[diff]), 2)
                        seen.add(diff)
                else:
                    count += (len(dic[diff]*len(dic[t[i]])))
                    seen.add(diff)
                    seen.add(t[i])

        return count


