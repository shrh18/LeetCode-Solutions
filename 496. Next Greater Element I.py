class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ret = []
        dic = defaultdict(int)
        for i in range(len(nums2)):
            j = i+1
            while j<len(nums2) and nums2[j]<nums2[i]:
                j += 1
            dic[nums2[i]] = nums2[j] if j<len(nums2) else -1
        for num in nums1:
            ret.append(dic[num])
        return ret