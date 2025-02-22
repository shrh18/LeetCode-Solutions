# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:

        def gotoParent(node):
            return gtp[node]

        def rec(node, currLevel, destLevel, q, val, parent):
            if len(q) == 0:
                node.val = val
                return
            node.val = val
            destLevel = 0
            while len(q)>0 and q[0] == '-':
                destLevel += 1
                q.popleft()
            v = ""
            while len(q)>0 and q[0] != '-':
                v += q.popleft()
            v = int(v)
            if destLevel == currLevel+1:
                print(f"Level: {destLevel}, val: {v}")
                print()
                if node.left == None:
                    node.left = TreeNode()
                    gtp[node.left] = node
                    rec(node.left, currLevel+1, destLevel, q, v, node)
                else:
                    node.right = TreeNode()
                    gtp[node.right] = node
                    rec(node.right, currLevel+1, destLevel, q, v, node)
            else:
                print(f"destLevel: {destLevel}")
                while destLevel != currLevel+1:
                    node = gotoParent(node)
                    currLevel -= 1
                print(f"reached node level: {currLevel} val: {node.val}")
                print()
                if node.left == None:
                    node.left = TreeNode()
                    gtp[node.left] = node
                    rec(node.left, currLevel+1, destLevel, q, v, node)
                else:
                    node.right = TreeNode()
                    gtp[node.right] = node
                    rec(node.right, currLevel+1, destLevel, q, v, node)

        q = deque(list(traversal))
        print(q)
        print()
        gtp = defaultdict(TreeNode)
        v = ""
        while len(q)>0 and q[0] != '-':
            v += q.popleft()
        root = TreeNode()
        rec(root, 0, None, q, int(v), None)
        return root
                

