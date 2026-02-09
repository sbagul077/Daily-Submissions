# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = []
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.result = list()
        if root is None:
            return self.result
        
        self.helper(root, 0)
        return self.result
    
    def helper(self, root: Optional[TreeNode], level: int) -> None:
        #base 
        if root is None:
            return
        
        if len(self.result) <= level:
            li = list()
            self.result.append(li)
        
        self.result[level].append(root.val)

        self.helper(root.left, level + 1)
        self.helper(root.right, level + 1)

#Time Complexity: O(n)
#Space Complexity: O(n)