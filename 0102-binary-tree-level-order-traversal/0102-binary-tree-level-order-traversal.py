# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = []
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        self.result = []
        
        if root is None:
            return self.result
        
        self.dfs(root, 0)
        
        return self.result
    
    def dfs(self, root, level):
        if root is None:
            return 
        
        if level == len(self.result):
            self.result.append([])
        
        self.result[level].append(root.val)
        
        self.dfs(root.left, level + 1)
        self.dfs(root.right, level + 1)
        
            
#DFS
#Time Complexity: O(n)
#Space Complexity: O(h)