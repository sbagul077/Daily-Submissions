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
    public ListNode reverseList(ListNode head) {
        if(head == null || head.next == null){
            return head;
        }
        Stack<ListNode> st = new Stack<ListNode>();

        ListNode curr = head.next;
        
        while(curr != null){
            head.next = null;
            st.push(head);
            head = curr;
            curr = curr.next;
        }

        curr = head;

        while(!st.isEmpty()){
            curr.next = st.pop();
            curr = curr.next;
        }

        return head;        
    }
}
// Using Stack
// Time Complexity: O(n)
// Space Complexity: O(n)