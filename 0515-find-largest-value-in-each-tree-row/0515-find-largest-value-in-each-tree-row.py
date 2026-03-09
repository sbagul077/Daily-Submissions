# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result = list()
        if root is None:
            return result
        
        # result.append(root.val)
        queue = deque()

        queue.append(root)

        while len(queue) > 0:
            size = len(queue)
            tempMax = float("-inf")

            for i in range(size):
                curr = queue.popleft()

                if curr.val > tempMax:
                    tempMax = curr.val
                
                if curr.left:
                    queue.append(curr.left)
                
                if curr.right:
                    queue.append(curr.right)

            result.append(tempMax)

        return result

# Time Complexity: O(n)
# Space Complexity: O(n)