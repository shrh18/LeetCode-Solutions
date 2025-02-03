class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        
        def generateNums(s):
            nums = []
            n = len(s)
            if isValid(s): nums.append(s)
                
            for i in range(1, n):
                intPart = s[:i]
                fracPart = s[i:n]

                if isValid(intPart) and isValid(fracPart, True):
                    nums.append(f"{intPart}.{fracPart}")
            return nums
        
        def isValid(s, isFrac = False):
            if not s:
                return False
            if not isFrac:
                if s[0] == '0' and len(s)>1:
                    return False
            if isFrac:
                if s[-1] == '0':
                    return False
            return True

        ret = []
        s = s[1:-1]
        for i in range(1, len(s)):
            str1 = s[:i]
            str2 = s[i:]

            nums1 = generateNums(str1)
            nums2 = generateNums(str2)

            for num1 in nums1:
                for num2 in nums2:
                    ret.append(f"({num1}, {num2})")

        return ret
