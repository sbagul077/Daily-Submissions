# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    first = 0
    second = 0
    flag = False
    prev = 0
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return 
        
        self.inorder(root)
        print(self.first.val, self.second.val)
        temp = self.first.val
        self.first.val = self.second.val
        self.second.val = temp       
    
    def inorder(self, root):
        if root is None:
            return
        
        self.inorder(root.left)
        
        if self.prev and self.prev.val > root.val:
            if not self.flag:
                self.first = self.prev
                self.second = root
                self.flag = True
            else:
                self.second = root
        self.prev = root
        self.inorder(root.right)
            
        
#inorder recursion
# Time Complexity : O(n)
# Space Complexity: O(1)
            