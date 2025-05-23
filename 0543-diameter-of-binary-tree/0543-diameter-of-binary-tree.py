# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.dfs(root)
        return self.diameter
        
    def dfs(self, root):
        if root is None:
            return 0
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        self.diameter = max(self.diameter, left + right)
        return 1 + max(left, right)

