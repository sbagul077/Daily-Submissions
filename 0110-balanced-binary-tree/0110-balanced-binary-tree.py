# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        return self.height(root) != -1

    def height(self, root):
        if root is None:
            return 0
        
        left = self.height(root.left)
        right = self.height(root.right)

        if abs(left - right) > 1:
            return -1
        
        if left == -1 or right == -1:
            return -1
        
        return max(self.height(root.left), self.height(root.right)) + 1