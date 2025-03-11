class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        if k > len(colors):
            return 0
        count = 0
        n = colors
        n.extend(colors[:k-1])
        # print(n)
        l = 0
        for i in range(1, len(n)):
            if i-l+1<=k:
                if n[i] == n[i-1]:
                    l = i

            if i-l+1 == k:
                count += 1
                l += 1

        return count