# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = 0
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0
        
        self.result = set()
        return self.dfs(root, 0)

    
    def dfs(self, root, num):
        #base case
        if root is None:
            return 0
        
        if root.right is None and root.left is None:
            return num * 10 + root.val

        return self.dfs(root.left, num * 10 + root.val) + self.dfs(root.right, num * 10 + root.val)
        