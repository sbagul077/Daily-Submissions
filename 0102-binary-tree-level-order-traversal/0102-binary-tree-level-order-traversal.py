# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        result = []
        
        queue = deque()
        queue.append(root)
        
        while queue:
            size = len(queue)
            li = []
            for i in range(size):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                
                if curr.right:
                    queue.append(curr.right)
                li.append(curr.val)
            
            result.append(li)
        
        return result
    
# Time complexity: O(n)
# Space Complexity: O(n)