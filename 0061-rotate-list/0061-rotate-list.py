# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k == 0:
            return head

        count = 1

        curr = head

        while curr.next:
            count += 1
            curr = curr.next
        
        k = count - (k % count)

        curr.next = head

        while k > 0:
            curr = curr.next
            k -= 1
        head= curr.next
        curr.next = None

        return head

