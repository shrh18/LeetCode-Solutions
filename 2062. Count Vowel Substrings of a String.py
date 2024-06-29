class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        def checkVowel(substring):
            vowels = {'a', 'e', 'i', 'o', 'u'}
            return vowels.issubset(set(substring))
        
        vowels = {'a', 'e', 'i', 'o', 'u'}
        word = list(word)
        n = len(word)
        count = 0
        
        for left in range(n):
            if word[left] in vowels:
                tempStr = ""
                for pointer in range(left, n):
                    if word[pointer] in vowels:
                        tempStr += word[pointer]
                        if len(tempStr) >= 5 and checkVowel(tempStr):
                            count += 1
                    else:
                        break

        return count