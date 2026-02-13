# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = []
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.result = []
        
        if root is None:
            return self.result
        
        self.dfs(root, 1)

        return self.result
    
    def dfs(self, root: Optional[TreeNode], level: int) -> None:
        #base
        if root is None:
            return

        if len(self.result) < level:
            self.result.append(root.val)

        self.dfs(root.right, level + 1)
        self.dfs(root.left, level + 1)
    
#DFS
# Time Complexity: O(N)
# Space Complexity: O(H)