"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None

        queue = deque()
        queue.append(root)

        while queue:
            size = len(queue)
            currRoot = queue.popleft()

            if(currRoot.left):
                queue.append(currRoot.left)
            
            if currRoot.right:
                queue.append(currRoot.right)
            
            for i in range(1, size):
                temp = queue.popleft()

                currRoot.next = temp
                currRoot = temp

                if currRoot.left:
                    queue.append(currRoot.left)
                
                if currRoot.right:
                    queue.append(currRoot.right)
        
        return root
    
#BFS
#TC: O(n)
#SC: O(n)