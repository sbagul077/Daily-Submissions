# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if inorder is None or len(inorder) == 0 or postorder is None or len(postorder) == 0:
            return None
        
        rootVal = postorder[-1]
        root = TreeNode(rootVal)
        rootIdx = 0
        
        for i in range(len(inorder)):
            if inorder[i] == rootVal:
                rootIdx = i
                break
        
        inLeft = inorder[0: rootIdx]
        inRight = inorder[rootIdx + 1 : ]
        postLeft = postorder[0 : rootIdx]
        postRight = postorder[rootIdx : len(postorder) - 1]
        
        root.left = self.buildTree(inLeft, postLeft)
        root.right = self.buildTree(inRight, postRight)
        
        return root

#Recursion
#Time Complexity: O(n^2)
#Space Complexity: O(n^2)