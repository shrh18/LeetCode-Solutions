# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.totMax = float('-inf')

        def dfs(node):
            if not node:
                return 0

            leftSum, rightSum = 0, 0
            if node:
                val = node.val
            if node.left:
                leftSum = max(dfs(node.left), 0)
            if node.right:
                rightSum = max(dfs(node.right), 0)

            tot = leftSum + rightSum + val

            if tot>self.totMax:
                self.totMax = tot
            
            return (max(leftSum, rightSum))+val
        
        dfs(root)
        return self.totMax