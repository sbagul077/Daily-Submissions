# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = list()
        if root is None:
            return result
        q = collections.deque()
        q.append(root)
        
        while q:
            # curr = q.popleft()
            size = len(q)
            li = list()
            for i in range(size):
                curr = q.popleft()
                li.append(curr.val)
                
                if curr.left:
                    q.append(curr.left)
                
                if curr.right:
                    q.append(curr.right)
            
            result.append(li)
        
        return result

#BFS
#Time Complexity: O(n)
#Space Complexity: O(n)
                