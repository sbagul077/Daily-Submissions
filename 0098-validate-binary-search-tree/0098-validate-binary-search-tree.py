# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev = None
    # result = True
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # self.result = True
        prev = None

        return self.inorder(root)

        # return self.result
            
    def inorder(self, root):
        if root is None:
            return True
        
        if not self.inorder(root.left):
            return False

        if self.prev is not None and self.prev.val >= root.val:
            return False
        self.prev = root
        return self.inorder(root.right)

# [50, 40, 60, 35, 45, null, 65, 30, 38, 42,46,62,68]