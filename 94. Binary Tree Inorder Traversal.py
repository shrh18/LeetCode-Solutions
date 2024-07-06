# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        order = []
        
        def traverse(root):
            if root is None:
                return
            
            traverse(root.left)
            order.append(root.val)
            traverse(root.right)

        traverse(root)
        print(order)
        return order