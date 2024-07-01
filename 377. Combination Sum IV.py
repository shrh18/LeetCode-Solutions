class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        paths = {0:1}
        for tot in range(1, target+1):
            paths[tot] = 0
            for n in nums:
                paths[tot] += paths.get(tot-n, 0)
        print(paths[target])
        return paths[target]

                    