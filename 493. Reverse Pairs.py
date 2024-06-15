class Solution:
    def __init__(self):
        self.count = 0
    
    def spl(self, arr, low, high):
        if low >= high:
            return
        mid = (low + high) // 2
        self.spl(arr, low, mid)
        self.spl(arr, mid + 1, high)
        self.merge(arr, low, mid, high)

    def merge(self, arr, low, mid, high):
        temp = []
        left = low
        right = mid + 1
        
        # Count reverse pairs
        for i in range(left, mid + 1):
            while right <= high and arr[i] > 2 * arr[right]:
                right += 1
            self.count += (right - (mid + 1))
        
        # Reset the pointers to merge the arrays
        left = low
        right = mid + 1
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1
                
        while left <= mid:
            temp.append(arr[left])
            left += 1
        while right <= high:
            temp.append(arr[right])
            right += 1
        
        for i in range(len(temp)):
            arr[i + low] = temp[i]
    
    def reversePairs(self, nums):
        if not nums:
            return 0
        self.spl(nums, 0, len(nums) - 1)
        return self.count
