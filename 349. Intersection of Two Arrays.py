class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        if len(nums1)>len(nums2):
            nums1, nums2 = nums2, nums1
        l, r = 0, 0
        ret = set()
        while l<len(nums1):
            if l==len(nums1) or r == len(nums2):
                break
                
            if nums1[l] == nums2[r]:
                ret.add(nums1[l])
                l += 1
                r += 1
            elif nums1[l]<nums2[r]:
                l += 1
            else:
                r += 1
        return list(ret)

