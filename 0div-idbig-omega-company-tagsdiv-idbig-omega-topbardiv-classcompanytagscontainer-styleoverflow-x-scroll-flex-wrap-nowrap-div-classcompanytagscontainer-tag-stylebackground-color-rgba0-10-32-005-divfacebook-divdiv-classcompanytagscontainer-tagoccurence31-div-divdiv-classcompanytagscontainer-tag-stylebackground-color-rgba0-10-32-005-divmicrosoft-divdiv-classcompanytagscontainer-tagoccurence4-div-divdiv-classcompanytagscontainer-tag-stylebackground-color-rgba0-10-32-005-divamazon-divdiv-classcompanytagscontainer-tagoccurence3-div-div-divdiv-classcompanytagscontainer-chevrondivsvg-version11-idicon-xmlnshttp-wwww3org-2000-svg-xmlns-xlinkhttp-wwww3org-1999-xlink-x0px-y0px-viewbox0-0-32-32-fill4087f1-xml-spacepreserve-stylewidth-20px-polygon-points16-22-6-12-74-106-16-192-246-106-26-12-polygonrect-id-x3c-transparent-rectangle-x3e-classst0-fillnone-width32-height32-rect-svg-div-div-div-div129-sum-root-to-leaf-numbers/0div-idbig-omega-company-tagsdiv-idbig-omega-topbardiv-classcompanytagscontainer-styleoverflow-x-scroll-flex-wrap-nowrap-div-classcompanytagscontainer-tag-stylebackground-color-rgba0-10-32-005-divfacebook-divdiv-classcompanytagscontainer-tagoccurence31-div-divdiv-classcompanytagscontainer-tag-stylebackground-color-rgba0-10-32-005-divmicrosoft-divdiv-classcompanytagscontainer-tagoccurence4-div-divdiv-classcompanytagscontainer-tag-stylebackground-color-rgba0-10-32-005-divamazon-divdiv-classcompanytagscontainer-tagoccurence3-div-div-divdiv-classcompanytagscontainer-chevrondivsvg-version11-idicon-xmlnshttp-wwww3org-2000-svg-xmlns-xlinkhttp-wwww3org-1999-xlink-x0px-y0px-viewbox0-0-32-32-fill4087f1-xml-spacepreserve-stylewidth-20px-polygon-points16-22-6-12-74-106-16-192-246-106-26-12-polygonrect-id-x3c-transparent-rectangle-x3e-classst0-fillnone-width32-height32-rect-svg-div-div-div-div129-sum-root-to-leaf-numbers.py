# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = 0
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        st = list()
        numStack = list()
        num = 0
        result = 0
        
        while root or st:
            while root:
                st.append(root)
                num = num * 10 + root.val
                numStack.append(num)
                root = root.left
            
            root = st.pop()
            num = numStack.pop()
            if root.right is None and root.left is None:
                result += num
            
            root = root.right
        return result