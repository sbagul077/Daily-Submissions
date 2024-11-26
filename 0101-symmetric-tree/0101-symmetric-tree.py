# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # isValid = None 
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        # self.isValid = True
        
        return self.dfs(root.left, root.right)
        # return self.isValid
                
    def dfs(self, left, right):
        # base
        if left is None and right is None:
            return True
        
        if left is None or right is None or left.val != right.val:
            # self.isValid = False
            return False
        
        return self.dfs(left.left, right.right) and self.dfs(left.right, right.left)