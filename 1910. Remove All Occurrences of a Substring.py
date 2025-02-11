class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        s = list(s)
        part = list(part)

        stack = []

        for i in range(len(s)):
            stack.append(s[i])
            if len(stack)>=len(part):
                if stack[-len(part):] == part:
                    stack = stack[:-len(part)]
        
        return "".join(stack)

