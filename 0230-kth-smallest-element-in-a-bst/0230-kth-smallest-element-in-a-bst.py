# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result= 0
    count = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.result = 0
        self.count = k
        self.inorder(root)
        return self.result
        
    def inorder(self,root):
        #base case
        if root is None:
            return
        #logic
        self.inorder(root.left)
        self.count -= 1
        if self.count == 0:
            self.result = root.val
        
        self.inorder(root.right)
        

        