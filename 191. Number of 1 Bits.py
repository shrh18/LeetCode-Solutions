class Solution:
    def hammingWeight(self, n: int) -> int:
        d = defaultdict(list)
        arr = Counter((bin(n))[2:])
        return arr['1']
        