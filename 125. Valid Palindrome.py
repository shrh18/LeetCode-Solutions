class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []
        def isPal(arr):
            n = len(arr)
            for i in range(n//2):
                if arr[i]!=arr[n-1-i]:
                    return False
            return True
        
        for ch in s:
            if ch.isalnum():
                arr.append(ch.lower())

        return isPal(arr)