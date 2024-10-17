# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return None

        adjl = {}
        def dfs(node, parent):
            if not node:
                return

            if node.val in adjl:
                adjl[node.val].append(parent.val)
            else:
                adjl[node.val] = [parent.val]

            adjl[parent.val].append(node.val)

            dfs(node.left, node)
            dfs(node.right, node)
                
        adjl[root.val] = []
        dfs(root.left, root)
        dfs(root.right, root)
        print(adjl)

        queue = [target.val]
        visited = set(queue)
        currDis = 0

        while queue:
            if currDis == k:
                return queue
            
            nextqueue = []
            for node in queue:
                for nei in adjl[node]:
                    if nei not in visited:
                        visited.add(nei)
                        nextqueue.append(nei)

            queue = nextqueue
            currDis+=1
        
        return []
        
        