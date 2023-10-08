# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = []
    target = 0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return list()
        
        self.target = targetSum
        self.result = list()
        
        self.dfs(root, 0, path = [])
        
        return self.result
    
    def dfs(self, root, currSum, path):
        #base 
        if root is None:
            return 
        
        currSum = currSum + root.val
        path.append(root.val)
        
        if root.left is None and root.right is None and currSum == self.target:
            self.result.append(path)
        
        self.dfs(root.left, currSum, path.copy())
        self.dfs(root.right, currSum, path.copy())
        
#DFS
#Time Complexity: O(n^2)
#Space Complexity: O(h)