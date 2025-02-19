class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []
        ret = []
        i = 1
        for ch in pattern:
            stack.append(i)
            i += 1
            if ch == 'I':
                while len(stack)>0:
                    ret.append(str(stack.pop()))

        stack.append(i)
        while len(stack)>0:
            ret.append(str(stack.pop()))

        return "".join(ret)


        