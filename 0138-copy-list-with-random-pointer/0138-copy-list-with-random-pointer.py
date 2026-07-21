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
        if head is None:
            return None
        
        curr = head

        #Step 1: Create a deep copy of the original list 
        while curr:
            copyNode = Node(curr.val)
            copyNode.next = curr.next
            curr.next = copyNode
            curr = curr.next.next
        
        #Step 2: point randon pointers on copied list same as original list

        curr = head
        
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        #Step 3: Seperate original list with copied one

        curr = head
        copyHead = curr.next
        currCopy = curr.next

        while curr:
            curr.next = curr.next.next
            if currCopy.next:
                currCopy.next = currCopy.next.next
            curr = curr.next
            currCopy = currCopy.next
        
        return copyHead
            