# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = 0
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        
        self.helper(root, 0)
        
        return self.result
    
    def helper(self, root, sumRoot):
        #base case
        if root is None:
            return
        #logic
        
       
        self.helper(root.left, (sumRoot * 10) + root.val)
        
        if root.right is None and root.left is None:
            self.result += (sumRoot * 10) + root.val
            return

        self.helper(root.right, (sumRoot * 10) + root.val)
    
        
        return