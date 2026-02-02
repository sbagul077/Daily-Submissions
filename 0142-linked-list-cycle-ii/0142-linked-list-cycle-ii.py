# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        slow = head
        fast = head
        flag = False
        # Detect cycle using slow at 1x and fast at 2x speed 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                flag = True
                break

        if not flag:
            return None
        #  reset slow to head
        slow = head
#  where ever the slow and fast meets that's the node where cycle begins.
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow

# Time Complexity: O(n)
# Space Complexity: O(1)

