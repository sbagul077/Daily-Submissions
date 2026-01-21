# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = list()
    path = list()
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.result = list()
        self.path = list()
        self.target = targetSum
        self.helper(root, 0)
        return self.result
    
    def helper(self, root, currSum):
        if root is None:
            return
        
        self.path.append(root.val)
        currSum += root.val

        if not root.left and not root.right and self.target == currSum:
            self.result.append(self.path.copy())

        self.helper(root.left, currSum)
        self.helper(root.right, currSum)
        # print(self.path, "Before")
        self.path.pop()
        # print(self.path, "After")