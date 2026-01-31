# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        return self.helper(root.left, root.right)
    
    def helper(self, left, right):
        #base
        if left is None and right is None:
            return True


        #logic
        if left is None or right is None or left.val != right.val:
            return False
        
        return self.helper(left.left, right.right) and self.helper(left.right, right.left)

# DFS
# Time Complexity: O(n)
# @Space Complexity: O(n)