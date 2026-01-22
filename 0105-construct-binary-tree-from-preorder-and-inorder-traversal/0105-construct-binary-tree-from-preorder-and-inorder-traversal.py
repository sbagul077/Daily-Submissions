# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    hashMap = dict()
    idx = 0
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.hashMap = dict()
        idx = 0
        
        for index, value in enumerate(inorder):
            self.hashMap[value] = index

        return self.helper(preorder, inorder, 0, len(inorder) - 1)
    
    def helper(self, preorder, inorder, start, end):
        #base
        if start > end:
            return None
        #logic
        root = TreeNode(preorder[self.idx])
        rootIdx = self.hashMap.get(preorder[self.idx])
        self.idx += 1

        root.left = self.helper(preorder, inorder, start, rootIdx - 1)
        root.right = self.helper(preorder, inorder, rootIdx + 1, end)
        return root