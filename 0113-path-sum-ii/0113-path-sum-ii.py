# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = []
    path = []
    target = 0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.result = []
        self.target = targetSum
        self.path = []
        
        self.helper(root, 0)
        return self.result
    
    def helper(self,root, total):
        #base
        if root is None:
            return 
        
        self.path.append(root.val)
        total = total + root.val
        
        if root.right is None and root.left is None:
            if total == self.target:
                self.result.append(self.path.copy())            
        
        self.helper(root.left, total)
        self.helper(root.right, total)
        self.path.pop(-1)

           