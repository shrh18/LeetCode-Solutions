class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:

        ret = []
        while nums1 and nums2:
            if nums1[0][0] < nums2[0][0]:
                ret.append(nums1[0])
                del nums1[0]
            elif nums1[0][0] == nums2[0][0]:
                ret.append([nums1[0][0], nums1[0][1]+nums2[0][1]])
                del nums1[0]
                del nums2[0]
            else:
                ret.append(nums2[0])
                del nums2[0]

        while nums1:
            ret.append(nums1[0])
            del nums1[0]
        
        while nums2:
            ret.append(nums2[0])
            del nums2[0]

        return ret

