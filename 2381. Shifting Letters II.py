class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        s = list(s)
        lets = list(string.ascii_lowercase)
        dic = defaultdict(int)
        for i, char in enumerate(lets):
            dic[char] = i
        pre = [0]*(len(s)+1)
        s = [dic[char] for char in s]      

        for start, end, direc in shifts:
            if direc == 0:
                pre[start] += 1
                pre[end+1] -= 1
            else:
                pre[start] -= 1
                pre[end+1] += 1

        diff = pre[-1]
        for i in range(len(s)-1, -1, -1):
            s[i] = s[i] + diff
            diff += pre[i]

        return "".join([lets[i%26] for i in s])