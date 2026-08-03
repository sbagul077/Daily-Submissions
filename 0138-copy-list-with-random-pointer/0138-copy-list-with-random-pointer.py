"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None :
            return head
        
        # 1. Make a deep of just the list
        curr = head

        while curr:
            copyNode = Node(curr.val)
            copyNode.next = curr.next
            curr.next = copyNode
            curr = curr.next.next

        # 2. Point the random pointers to the copied list
        curr = head
        # print(curr.val)
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # 3. seperate two list
        curr = head
        currCopy = head.next
        head2 = head.next
  
        while curr:
            curr.next = curr.next.next
            if currCopy.next:
                currCopy.next = currCopy.next.next                
            curr = curr.next
            currCopy = currCopy.next
        # print(head2, head)
        return head2

#Pointers        
# Time Complexity: O(n)
#Space Complexity: O(1)