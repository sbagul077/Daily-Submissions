# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        st = []
        numstack = []
        num = 0
        s = 0
        
        while root or st:
            while root:  
                num = root.val + (num * 10)
                numstack.append(num)
                st.append(root)
                root = root.left       
            
            root = st.pop()
            num = numstack.pop()
            
            if root.right is None and root.left is None:
                s += num
            root = root.right
        
        return s