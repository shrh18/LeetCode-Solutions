class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n-1
        vol = []
        while l<r:
            vol.append((r-l)*(min(height[l], height[r])))
            if height[r]<height[l]:
                r-=1
            else:
                l+=1

        return max(vol)
