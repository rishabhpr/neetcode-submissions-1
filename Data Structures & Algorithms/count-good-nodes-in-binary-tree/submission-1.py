# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, max_seen):
            if not node:
                return 0
            
            good = 0

            if node.val >= max_seen:
                good = 1

            new_max = max(node.val, max_seen)

            left = dfs(node.left, new_max)
            right = dfs(node.right, new_max)

            return good + left+ right
        
        return dfs(root, root.val)

        