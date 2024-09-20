# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def travel(node, subnode):
            if not node and not subnode:
                return True
            elif not node or not subnode:
                return False
            elif node.val!=subnode.val:
                return False
            return travel(node.left, subnode.left) and travel(node.right, subnode.right)

        def travelTill(node):
            if not node:
                return False

            if travel(node, subRoot):
                print(f"val is {node.val}")
                return True
            
            return travelTill(node.right) or travelTill(node.left)

        return travelTill(root)

            
        