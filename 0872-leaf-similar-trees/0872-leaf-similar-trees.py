# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 is None or root2 is None:
            return False
    
        arr_1 = list()
        arr_2 = list()
        self.helper(root1, arr_1)
        self.helper(root2, arr_2)
        
        return arr_1 == arr_2
        
    def helper(self, root, arr):
        if root is None:
            return
        
        if root.right is None and root.left is None:
            arr.append(root.val)
            return
    
        self.helper(root.left, arr)
        self.helper(root.right, arr)
        
#DFS
#Time Complexity: O(m + n)
#Space Complexity: O(m + n)