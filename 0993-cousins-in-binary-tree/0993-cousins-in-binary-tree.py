# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    x_parent = None
    y_parent = None
    x_level = 0
    y_level = 0
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if root is None:
            return False

        self.x_parent = None
        self.y_parent = None
        self.x_level = 0
        self.y_level = 0

        self.dfs(root, 1, x, y, None)

        return self.x_parent != self.y_parent and self.x_level == self.y_level

    
    def dfs(self, root, level, x, y, parent):
        if root is None:
            return
        
        if root.val == x:
            self.x_parent = parent
            self.x_level = level
        
        if root.val == y:
            self.y_parent = parent
            self.y_level = level
        
        self.dfs(root.left, level + 1, x, y, root)
        self.dfs(root.right, level + 1, x, y, root)