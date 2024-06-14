class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        for dig in digits:
            num += str(dig)
        num = int(num) + 1
        num = str(num)
        ret = [0]*len(num)
        for i in range(len(num)):
            ret[i] = int(num[i])
        return ret