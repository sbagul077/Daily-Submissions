# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        
        prev = None
        curr = head
        fast = head.next
        
        while fast:
            curr.next = prev
            prev = curr
            curr = fast
            fast = fast.next
            
        curr.next = prev
        
        return curr
    
#3 pointers
# TC :O(n)
# SC: O(1). No extra space
