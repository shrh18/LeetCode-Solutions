class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if len(s) == 0:
            return ""
        if len(s) == 1:
            return s
        
        stack = []
        stack.append([s[0], 1])

        for i in range(1, len(s)):
            if stack and s[i] == stack[-1][0]:
                stack[-1][1] += 1
            else:
                stack.append([s[i], 1])

            if stack[-1][1] == k:
                stack.pop()

        ret = ""
        for pair in stack:
            ret += pair[0]*pair[1]

        return ret