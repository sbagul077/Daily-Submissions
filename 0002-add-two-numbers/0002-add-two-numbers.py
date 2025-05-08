# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None or l2 is None:
            return 0
        
        dummy = ListNode()
        temp = dummy
        currSum = 0
        
        while (l1 != None or l2 != None) or currSum:
            total = 0
            if l1 != None:
                total += l1.val
                l1 = l1.next
            if l2 != None:
                total += l2.val
                l2 = l2.next
            
            total += currSum
            currSum = total // 10
            node = ListNode(total % 10)
            temp.next = node
            temp = temp.next
        
        return dummy.next

#maths
#Time Complexity: O(m + n)
#Space Complexity :O(1)