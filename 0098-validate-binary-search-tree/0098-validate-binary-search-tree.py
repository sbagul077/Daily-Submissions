# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        return self.helper(root, None, None)
    
    def helper(self, root, minimum, maximum):
        if root is None:
            return True
        
        if maximum is not None and root.val >= maximum:
            return False
        
        if minimum is not None and root.val <= minimum:
            return False
        
        return self.helper(root.left, minimum, root.val) and self.helper(root.right, root.val, maximum)