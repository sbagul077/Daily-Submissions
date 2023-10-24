# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        q = collections.deque()
        
        q.append(root)
        result = []
        
        while q:
            row_max = q[0].val
            size = len(q)
            for i in range(size):
                curr = q.popleft()
                row_max = max(row_max, curr.val)                
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            result.append(row_max)
        return result