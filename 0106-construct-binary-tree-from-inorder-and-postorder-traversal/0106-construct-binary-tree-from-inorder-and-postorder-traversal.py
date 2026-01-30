# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    hashMap = dict()
    idx = 0
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.idx = len(postorder) - 1
        # self.hashMap = dict()

        for index, value in enumerate(inorder):
            self.hashMap[value] = index
        
        return self.helper( inorder, postorder, 0, len(inorder) - 1)
    
    def helper(self,inorder, postorder, start, end):
        #base
        if start > end:
            return None
        # print(self.idx)
        root = TreeNode(postorder[self.idx])
        rootIdx = self.hashMap.get(postorder[self.idx])
        self.idx -= 1

        root.right = self.helper(inorder, postorder, rootIdx + 1, end)
        root.left = self.helper(inorder, postorder, start, rootIdx - 1)

        return root

#hashMap
#time complexity: O(n)
#Space complexity: O(n)