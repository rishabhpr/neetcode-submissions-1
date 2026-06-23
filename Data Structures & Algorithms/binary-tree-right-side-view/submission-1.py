# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        result = []

        queue = deque([root])

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                current = queue.popleft()

                if current:
                    current_level.append(current.val)
                
                    if current.left:
                        queue.append(current.left)

                    if current.right:
                        queue.append(current.right)
            
            result.append(current_level[-1])
        
        return result