# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.result = []
        self.dfs(root, 0)
        return self.result
    
    def dfs(self, node, level):
        if not node:
            return 
        
        if len(self.result) <= level:
            self.result.append([])
        
        self.result[level].append(node.val)
        
        self.dfs(node.left, level + 1)
        self.dfs(node.right, level + 1)
    
