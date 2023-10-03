# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    idx = 0
    hashMap = dict()
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if inorder is None or len(inorder) == 0 or postorder is None or len(postorder) == 0:
            return None
        
        self.idx = len(postorder) - 1
        self.hashMap = dict()
        
        for index, node in enumerate(inorder):
            self.hashMap[node] = index
            
        return self.helper(postorder, 0, len(postorder) - 1)
    
    def helper(self, postorder, start, end):
        #base
        if start > end or self.idx < 0:
            return None
        
        rootVal = postorder[self.idx]
        root = TreeNode(rootVal)
        self.idx -= 1
        
        rootIdx = self.hashMap.get(rootVal)
        
        root.right = self.helper(postorder, rootIdx + 1, end)
        root.left = self.helper(postorder, start, rootIdx - 1)
        
        return root

#Recursion, hashMap
#Time Complexity: O(n)
#Space Complexity: O(n)