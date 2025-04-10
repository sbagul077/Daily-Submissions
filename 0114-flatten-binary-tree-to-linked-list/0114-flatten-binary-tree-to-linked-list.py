# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        #base
        if root is None or root.right is None and root.left is None:
            return 
        
        #recursion

        if(root.left):
            self.flatten(root.left)
            tempNode = root.right
            root.right = root.left
            root.left = None
            while(root.right):
                root = root.right
            root.right = tempNode

        self.flatten(root.right)