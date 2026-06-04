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
        if root is None:
            return root
        
        self.inorder(root)
        temp = self.first.val
        self.first.val = self.second.val
        self.second.val = temp
    
    def inorder(self, root):
        if root is None:
            return 
        
        self.inorder(root.left)
        #st.pop()
        if(self.prev != None and self.prev.val >= root.val):
            if(self.flag == False):
                self.first = self.prev
                self.second = root
                self.flag = True
            else:
                self.second = root
        
        self.prev = root
        self.inorder(root.right)