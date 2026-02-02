// /
//   Definition for singly-linked list.
//   struct ListNode {
//       int val;
//       ListNode next;
//       ListNode(int x) : val(x), next(NULL) {}
//   };
//  /
class Solution {
    public ListNode detectCycle(ListNode head) {
        // if(head == null){
        //     return None;
        // }

        ListNode slow = head;
        ListNode fast = head;
        boolean flag = false;

        //detect cycle
        while(fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;

            if(slow == fast){
                flag = true;
                break;                    
            }
        }

        //if no cycle then return null
        if(flag == false){
            return null;
        }

        slow = head;

        //whereever the slow and fast meets that's the node where cycle begins 
        while(slow != fast){
            slow = slow.next;
            fast = fast.next;
        }
        return slow; 
    }
};