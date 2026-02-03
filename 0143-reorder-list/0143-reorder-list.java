/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public void reorderList(ListNode head) {
        if(head ==  null){
            // return head;
        }

        ListNode slow = head;
        ListNode fast = head;

        // find the middle node of the list
        while(fast != null && fast.next != null){
            slow = slow.next; // 1x speed
            fast = fast.next.next; //2x speed
        }

        ListNode head2 = reverse(slow.next);
        slow.next = null;

        ListNode curr = head;
        ListNode next1 = curr.next;
        ListNode temp = null;

        

        // System.out.println(head2.val);
        // System.out.println(curr.val);

        while(head2 != null){
            temp = head2.next;
            curr.next = head2;
            // System.out.println(curr.val + " curr.val");
            // System.out.println(curr.next.val + " curr.next");
            head2.next = next1;
            // System.out.println(head2.val + " head2 val");
            // System.out.println(head2.next.val + " head2 next val");
            curr = next1;
            // System.out.println(next1.val + " next1 val");
            // System.out.println(curr.val + " curr pointer same as next1");
            next1 = next1.next;
            head2 = temp;
        }
    }

    private ListNode reverse(ListNode head2){
        if(head2 == null){
            return head2;
        }
        ListNode prev = null;
        ListNode temp = head2.next;

        while(temp != null){
            head2.next = prev;
            prev = head2;
            head2 = temp;
            temp = temp.next;
        }
        head2.next = prev;

        return head2;
    }
}