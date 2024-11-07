# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev = None
    flag = None
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = None
        self.flag = True
        self.inorder(root)
        return self.flag
    
    def inorder(self, root):
        if root is None:
            return
        
        self.inorder(root.left)
        
        if self.prev and self.prev.val >= root.val:
            self.flag = False
        
        self.prev = root
        self.inorder(root.right)