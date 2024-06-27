from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        counts = [0]*len(nums)
        ll = SortedList()
        ll.add(nums[-1])
        for i in range(len(nums)-2, -1, -1):
            ll.add(nums[i])
            ind = ll.index(nums[i])
            counts[i] = ind
        return counts
