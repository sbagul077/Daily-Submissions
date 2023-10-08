# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = []
    target = 0
    path = []
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return list()
        
        self.path = []
        self.target = targetSum
        self.result = list()
        
        self.dfs(root, 0)
        
        return self.result
    
    def dfs(self, root, currSum):
        #base 
        if root is None:
            return 
        
        currSum = currSum + root.val
        self.path.append(root.val)
        
        if root.left is None and root.right is None and currSum == self.target:
            self.result.append(self.path.copy())
        
        self.dfs(root.left, currSum)
        self.dfs(root.right, currSum)
        self.path.pop()
        
#DFS
#Time Complexity: O(n)
#Space Complexity: O(h)