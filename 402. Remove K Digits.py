class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for ch in num:
            while k>0 and stack and stack[-1]>ch:
                k-=1
                stack.pop()
            stack.append(ch)
        stack = stack[:len(stack)-k]
        print("Stack - ", stack)
        res = "".join(stack)
        if res:
            res = list(res)
            i = 0
            while i < len(res):
                if res[i]=='0':
                    del res[i]
                else:
                    break
        res = "".join(res)
        return res if res else "0"

        
        
        