class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:

        def genbi(n):
            if n == 0:
                return [""]
            result = []
            for bit in ["0", "1"]:
                for string in genbi(n - 1):
                    result.append(bit + string)
            return result

        result = genbi(len(nums))

        for st in nums:
            if st in result:
                result.remove(st)

        return result.pop()     