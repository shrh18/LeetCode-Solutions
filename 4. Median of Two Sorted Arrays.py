class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = None
        B = None

        if len(nums1)<=len(nums2):
            A = nums1
            B = nums2
        else:
            A = nums2
            B = nums1
        lenA, lenB = len(A), len(B)
        imin, imax = 0, lenA

        while imin<=imax:
            i = int((imin+imax)//2)
            j = int((lenA + lenB + 1)//2 - i)

            if i>0 and A[i-1]>B[j]:
                imax = i - 1
            elif i<lenA and B[j-1]>A[i]:
                imin = i + 1
            else:
                if i==0: maxLeft = B[j-1]
                elif j==0: maxLeft = A[i-1]
                else: maxLeft = max(A[i-1], B[j-1])

                if (lenA+lenB)%2==1:
                    return maxLeft
                
                if i==lenA: minRight=B[j]
                elif j== lenB: minRight = A[i]
                else: minRight = min(A[i], B[j])

                return (maxLeft + minRight)/2

         