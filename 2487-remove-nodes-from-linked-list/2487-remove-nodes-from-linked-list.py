# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        st = []
        curr = head
        
        while curr:
            while st and curr.val > st[-1]:
                st.pop()
                
            st.append(curr.val)
            curr = curr.next
            
        dummy = ListNode()
        curr = dummy
        
        for i in st:
            curr.next = ListNode(i)
            curr = curr.next
        
        return dummy.next


# Monotonic Stack
# Time Complexity: O(n)
# Space Complexity: O(n)