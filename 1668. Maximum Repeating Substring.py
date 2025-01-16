class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        count = 0
        mm = 0

        for i in range(0, len(sequence)-len(word)+1):
            l, r = i, len(word)-1+i
            while r < len(sequence):
                if sequence[l:r+1] == word:
                    count += 1
                    mm = max(mm, count)
                    l = r+1
                    r = r + len(word)
                else:
                    count = 0
                    l += 1
                    r += 1
            count = 0
        return mm