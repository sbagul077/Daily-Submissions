# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None or l2 is None:
            return 0
        
        count = list()
        
        while l1:
            count.append(str(l1.val))
            l1 = l1.next
            
        count = count[::-1]
        
        count1 = list()
        
        while l2:
            count1.append(str(l2.val))
            l2 = l2.next
            
        count1 = count1[::-1]    
        
        count = int("".join(count))
        count1 = int("".join(count1))
        count += count1
        result = list()
        count = str(count)

        head = ListNode(None)
        curr = head
        for i in range(len(count)- 1, -1, -1):
            # print(count[i])
            head.next = ListNode(int(count[i]))
            head = head.next
            
            
        return curr.next
        