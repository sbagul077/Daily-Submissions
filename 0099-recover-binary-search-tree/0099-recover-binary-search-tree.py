# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    first = None
    second = None
    flag = False
    prev = None
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.inorder(root)
        # print(self.first, self.second)
        temp = self.first.val
        self.first.val = self.second.val
        self.second.val = temp

    def inorder(self, root):
        #base
        if root is None:
            return 
        
        # logic
        self.inorder(root.left)
        if self.prev is not None and self.prev.val > root.val:
            if not self.flag:
                self.first= self.prev
                self.second = root
                self.flag = True
            else:
                self.second = root
        self.prev = root
        # print(self.prev.val)
        self.inorder(root.right)
