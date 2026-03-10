# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = []
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        self.result = list()
        
        if not root:
            return self.result
        # self.result.append(/)
        self.helper(root, 1)

        return self.result
    
    def helper(self, root: Optional[TreeNode], level : int) -> None:
        #base
        if root is None:
            return
        #logic
        if level > len(self.result):
            self.result.append(root.val)
        
        if level <= len(self.result):
            if self.result[level - 1] < root.val:
                self.result[level - 1] = root.val
        
        self.helper(root.left, level + 1)
        self.helper(root.right, level + 1)

# DFS
#Time Complexity: O(n)
#Space Complexity: O(h)

        