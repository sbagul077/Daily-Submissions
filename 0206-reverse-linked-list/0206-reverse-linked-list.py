# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        q = []
        
        while head.next:
            q.append(head.val)
            head = head.next    
        # q.reverse()
        
        temp = head
        i = len(q) - 1
        # print(temp.val, head.val, i)
        while i >= 0:
            temp.next = ListNode(q[i])
            temp = temp.next
            i -= 1

        return head