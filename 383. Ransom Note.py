class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote)>len(magazine):
            return False
        
        rc = Counter(ransomNote)
        mc = Counter(magazine)

        for i in range(len(ransomNote)):
            if rc[ransomNote[i]] > mc[ransomNote[i]]:
                return False

        return True