class Solution:
    def clearDigits(self, s: str) -> str:
        count = 0
        q = deque()
        for i in range(len(s)):
            if s[i].isdigit():
                if len(q)>0:
                    q.pop()
            else:
                q.append(s[i])
                
        print(q)
        return "".join(q)



