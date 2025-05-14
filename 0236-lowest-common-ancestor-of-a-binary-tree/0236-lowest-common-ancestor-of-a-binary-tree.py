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
        
        if root is None or p.val is None or q.val is None:
            return root
        
        self.pathP = []
        self.pathQ = []

        self.dfs(root, p, q, path= list())
        # print(self.pathP)
        # print(self.pathQ)
        for i in range(len(self.pathP)):
            if self.pathP[i].val != self.pathQ[i].val:
                return self.pathP[i -1]
        
        return None
    
    def dfs(self, root, p, q, path):
        #base case
        if root is None:
            return

        if root.val == p.val:
            # print("this")
            self.pathP = path.copy()
            self.pathP.append(root)
            self.pathP.append(root)
            # print(self.pathP)


        elif root.val == q.val:
            self.pathQ = path.copy()
            self.pathQ.append(root)
            self.pathQ.append(root)

        #logic
        # print(path)
        #recurse
        path.append(root)
        self.dfs(root.left, p, q, path)
        #backtrack
        
        self.dfs(root.right, p, q, path)
        path.pop(-1)

