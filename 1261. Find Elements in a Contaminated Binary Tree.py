# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        root.val = 0
        self.ss = set()

        def dfs(node, val):
            node.val = val
            self.ss.add(node.val)
            print(val)
            if node.left:
                dfs(node.left, 2*(node.val)+1)
            if node.right:
                dfs(node.right, 2*(node.val)+2)

        dfs(root, 0)
        
    def find(self, target: int) -> bool:
        return True if target in self.ss else False
            
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)