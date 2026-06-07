# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        def isSameTree(left, right):
            if not left and not right:
                return True
            
            if not left or not right:
                return False
            
            if left.val != right.val:
                return False
            
            left_check = isSameTree(left.left, right.left)
            right_check = isSameTree(left.right, right.right)

            return left_check and right_check
        
        if subRoot is None:
            return True
        
        if root is None:
            return False

        return (
    isSameTree(root, subRoot) or
    self.isSubtree(root.left, subRoot) or
    self.isSubtree(root.right, subRoot)
)