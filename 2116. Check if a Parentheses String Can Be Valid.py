class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s)%2 == 1:
            return False
        if locked[0] == '1' and s[0] == ')':
            return False
        
        low = 0
        high = 0

        for i in range(len(s)):
            if s[i] == '(' and locked[i] == '1':
                low += 1
                high += 1
            elif s[i] == '(' and locked[i] == '0':
                low = max(low-1, 0)
                high += 1
            elif s[i] == ')' and locked[i] == '1':
                low = max(low-1, 0)
                high -= 1
            elif s[i] == ')' and locked[i] == '0':
                low = max(low-1, 0)
                high += 1

            if high<0:
                return False

        if low == 0:
            return True
        else:
            return False

        