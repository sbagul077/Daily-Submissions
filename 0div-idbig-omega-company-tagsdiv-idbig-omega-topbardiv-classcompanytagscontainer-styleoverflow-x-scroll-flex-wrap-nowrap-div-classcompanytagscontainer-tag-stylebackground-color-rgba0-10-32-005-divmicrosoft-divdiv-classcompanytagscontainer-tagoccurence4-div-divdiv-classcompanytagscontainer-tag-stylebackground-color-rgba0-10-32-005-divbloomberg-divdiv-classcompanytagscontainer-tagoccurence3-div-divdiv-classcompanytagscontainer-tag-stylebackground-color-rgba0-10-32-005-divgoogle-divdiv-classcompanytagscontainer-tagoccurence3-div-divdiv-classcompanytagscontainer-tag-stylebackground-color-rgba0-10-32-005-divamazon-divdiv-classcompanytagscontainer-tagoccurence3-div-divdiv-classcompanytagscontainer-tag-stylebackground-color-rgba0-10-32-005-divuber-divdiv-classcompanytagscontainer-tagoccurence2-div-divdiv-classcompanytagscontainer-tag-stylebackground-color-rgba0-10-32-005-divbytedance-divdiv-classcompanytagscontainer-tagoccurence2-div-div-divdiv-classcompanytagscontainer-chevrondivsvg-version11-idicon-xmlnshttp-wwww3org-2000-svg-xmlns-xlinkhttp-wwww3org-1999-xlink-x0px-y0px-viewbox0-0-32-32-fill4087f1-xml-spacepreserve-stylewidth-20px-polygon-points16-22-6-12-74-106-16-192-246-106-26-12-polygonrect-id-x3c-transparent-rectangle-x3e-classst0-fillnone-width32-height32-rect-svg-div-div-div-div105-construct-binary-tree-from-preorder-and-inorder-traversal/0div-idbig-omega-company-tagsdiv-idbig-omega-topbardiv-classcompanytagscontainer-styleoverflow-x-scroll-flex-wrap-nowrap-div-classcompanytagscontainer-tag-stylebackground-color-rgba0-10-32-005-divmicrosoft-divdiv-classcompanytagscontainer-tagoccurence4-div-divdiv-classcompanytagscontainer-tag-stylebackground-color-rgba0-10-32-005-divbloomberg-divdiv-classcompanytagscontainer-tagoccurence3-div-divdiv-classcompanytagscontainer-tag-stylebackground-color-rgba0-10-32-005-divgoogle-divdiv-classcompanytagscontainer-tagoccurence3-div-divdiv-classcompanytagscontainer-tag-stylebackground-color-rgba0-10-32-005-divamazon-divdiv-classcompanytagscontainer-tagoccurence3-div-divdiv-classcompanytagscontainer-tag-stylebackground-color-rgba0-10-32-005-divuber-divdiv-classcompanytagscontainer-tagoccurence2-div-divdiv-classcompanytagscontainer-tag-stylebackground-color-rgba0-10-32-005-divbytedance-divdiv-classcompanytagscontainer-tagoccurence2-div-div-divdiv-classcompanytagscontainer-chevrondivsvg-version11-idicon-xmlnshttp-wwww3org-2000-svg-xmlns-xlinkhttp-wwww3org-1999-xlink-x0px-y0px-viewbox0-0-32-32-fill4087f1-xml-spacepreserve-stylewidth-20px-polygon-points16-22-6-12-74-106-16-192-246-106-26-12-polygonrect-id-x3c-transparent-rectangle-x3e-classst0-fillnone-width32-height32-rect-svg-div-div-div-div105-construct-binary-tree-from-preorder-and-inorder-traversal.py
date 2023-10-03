# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    idx = 0
    hashMap = dict()
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if preorder is None or len(preorder) == 0 or inorder is None or len(inorder) == 0:
            return None
        
        self.idx = 0
        self.hashMap = dict()
        
        for idx, node in enumerate(inorder):
            self.hashMap[node] = idx

        
        return self.helper(preorder, 0, len(inorder) - 1)
    
    def helper(self, preorder, start, end):
        if start > end:
            return None
        
        rootVal = preorder[self.idx]
        root = TreeNode(rootVal)
        self.idx += 1
        rootIdx = self.hashMap[rootVal]
        
        root.left = self.helper(preorder, start, rootIdx - 1)
        root.right = self.helper(preorder, rootIdx + 1, end)
        
        return root
        

#Recursion
#Time Complexity: O(n)
#Space Complexity: O(n)