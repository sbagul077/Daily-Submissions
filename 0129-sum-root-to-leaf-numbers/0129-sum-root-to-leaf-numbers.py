# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
       
        return self.helper(root, 0)
    
    def helper(self, root, sumRoot):
        #base case
        if root is None:
            return 0
        #logic
                
        if root.right is None and root.left is None:
            return (sumRoot * 10) + root.val

        return self.helper(root.left, (sumRoot * 10) + root.val) + self.helper(root.right, (sumRoot * 10) + root.val)
