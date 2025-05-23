# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        result = 0
        st = []

        while root or st:
            while root:
                st.append([root, len(st) + 1])
                root = root.left
        
            curr = st.pop()
            root = curr[0]

            if root.right is None and root.left is None:
                result = max(result, curr[1] + 1)
            
            root = root.right
        
        return result