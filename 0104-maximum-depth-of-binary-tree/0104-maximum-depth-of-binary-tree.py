# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        self.result = 0

        self.dfs(root, 0)
    
        return self.result
    
    def dfs(self, root: Optional[TreeNode], level: int) -> None:
        if root is None:
            return 


        if root.left is None and root.right is None:
            self.result = max(self.result, level + 1)
            return 
        
        self.dfs(root.left, level + 1)
        self.dfs(root.right, level + 1)