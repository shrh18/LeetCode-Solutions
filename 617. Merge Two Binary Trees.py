# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        if root1 and not root2:
            return root1
        if not root1 and root2:
            return root2
        
        def traverse(node1, node2):
            node1.val = node1.val + node2.val
            
            if node1.left and node2.left: 
                traverse(node1.left, node2.left)
            elif not node1.left and node2.left:
                node1.left = TreeNode(0)
                traverse(node1.left, node2.left)
            
            if node1.right and node2.right: 
                traverse(node1.right, node2.right)
            elif not node1.right and node2.right:
                node1.right = TreeNode(0)
                traverse(node1.right, node2.right)
        
        traverse(root1, root2)
        return root1
            
