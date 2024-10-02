# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        def bs(s, e):
            if s>e:
                return None
            mid = (s+e)//2
            node = TreeNode(nums[mid])

            node.left =  bs(s, mid-1)# left part including mid
            node.right = bs(mid+1, e) # right part excluding mid
    
            return node

        return bs(0, len(nums)-1)