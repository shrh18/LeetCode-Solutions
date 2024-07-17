from heapq import heapify, heappush, heappop

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or k==0:
            return []
        ret = []
        minHeap = []
        for i in range(min(k, len(nums1))):
            heappush(minHeap, (nums1[i]+nums2[0], i, 0))
        
        while k>0 and minHeap:
            valSum, i, j = heappop(minHeap)
            ret.append([nums1[i], nums2[j]])
            if j+1<len(nums2):
                heappush(minHeap, (nums1[i]+nums2[j+1], i, j+1))
            k-=1
        print(ret)
        return ret