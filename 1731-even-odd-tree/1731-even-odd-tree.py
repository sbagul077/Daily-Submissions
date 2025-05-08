# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue= deque()
        queue.append(root)
        level = 0
        prev = 0
        flag = "asc"

        while queue:
            size = len(queue)
            if level % 2 == 0:                
                flag = "asc"
                prev = -1
            else:
                prev = float("inf")
                flag = "desc"
            # print(level, flag)
            for i in range(size):
                curr = queue.popleft()
                
                if flag == "asc":
                    # print(curr.val, prev, flag, "asc")
                    if curr.val > prev and curr.val % 2 != 0:
                        prev = curr.val      
                    else:
                        return False                
                else:
                    # print(curr.val, prev, flag,"desc")
                    if curr.val < prev and curr.val % 2 == 0:
                        prev = curr.val
                    else:
                        return False
                
                if curr.left:
                    queue.append(curr.left)
                
                if curr.right:
                    queue.append(curr.right)
            
            level += 1
        
        return True


