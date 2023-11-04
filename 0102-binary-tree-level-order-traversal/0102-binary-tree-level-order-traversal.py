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
            li = list()
            size = len(q)
            
            for i in range(size):
                currNode = q.popleft()
                if currNode.left is not None:
                    q.append(currNode.left)
                    
                if currNode.right is not None:
                    q.append(currNode.right)
                
                li.append(currNode.val)
            
            result.append(li)
        
        return result

#BFS
#Time Complexity: O(n)
#Space Complexity: O(n).Size of the tree
                    