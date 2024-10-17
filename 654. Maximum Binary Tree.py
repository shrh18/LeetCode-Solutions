# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        def dac(st, en):
            if st>=en:
                return TreeNode(nums[st])

            arr = nums[st:en+1] 
            maxValIn = nums.index(max(arr))
            node = TreeNode(nums[maxValIn])

            node.left = dac(st, maxValIn-1) if st<maxValIn else None
            node.right = dac(maxValIn+1, en) if maxValIn<en else None

            return node

        maxValIn = nums.index(max(nums)) # 3
        node = TreeNode(nums[maxValIn])
        if maxValIn>0:
            node.left = dac(0, maxValIn-1)
        if maxValIn<len(nums)-1:
            node.right = dac(maxValIn+1, len(nums)-1)

        return node