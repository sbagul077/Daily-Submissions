# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = list()
        if root is None:
            return result

        q = deque()
        q.append(root)

        while q:
            size = len(q)
            
            for i in range(size):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                
                if curr.right:
                    q.append(curr.right)
                
                if i == (size - 1):
                    result.append(curr.val)
        return result

