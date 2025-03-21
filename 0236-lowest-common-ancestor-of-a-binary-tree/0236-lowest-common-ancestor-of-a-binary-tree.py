# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    pathP = []
    pathQ = []
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or p.val == root.val or q.val == root.val:
            return root
        
        self.backtrack(root, p, q, path = [])
        
        for i in range(len(self.pathP)):
            if self.pathP[i].val != self.pathQ[i].val:
                return self.pathP[i-1]
        return None
    
    def backtrack(self, root, p, q, path):
        #base case
        if root is None:
            return 
        
        if root.val == p.val:
            self.pathP = path.copy()
            self.pathP.append(p)
            self.pathP.append(p)
        
        if root.val == q.val:
            self.pathQ = path.copy()
            self.pathQ.append(q)
            self.pathQ.append(q)
        
        #action
        path.append(root)
        #recurse
        self.backtrack(root.left, p, q, path)
        self.backtrack(root.right, p, q, path)
        path.pop()