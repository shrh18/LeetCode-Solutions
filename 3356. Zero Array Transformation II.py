class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        diff = [0]*(len(nums)+1)
        ss, pos, n = 0, 0, len(nums)
        for i in range(n):
            while ss + diff[i] < nums[i]:
                if pos == len(queries):
                    return -1

                st = queries[pos][0]
                end = queries[pos][1]
                val = queries[pos][2]

                pos += 1

                if end < i:
                    continue

                diff[max(st, i)] += val
                diff[end+1] -= val

            ss += diff[i]

        return pos