class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:      
        # for char in letters:
        #     if char>target:
        #         return char
        # return letters[0]

        def rec(l, r):
            mid = (l+r)//2
            if l>=r:
                return letters[mid]
            if target<letters[mid]:
                return rec(l, mid)
            else:
                return rec(mid+1, r)

        if target>=letters[-1]:
            return letters[0]
        return rec(0, len(letters))
