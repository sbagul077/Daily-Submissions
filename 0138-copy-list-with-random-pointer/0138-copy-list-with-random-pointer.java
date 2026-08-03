/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        if(head == null){
            return head;
        }

        // 1. Create a deep copy of the original list
        Node curr = head;

        while(curr != null){
            Node currCopy = new Node(curr.val);
            currCopy.next = curr.next;
            curr.next = currCopy;
            curr = curr.next.next;
        }

        // 2. Point random pointers on the copied list same as the original list
        curr = head;

        while(curr != null){
            if(curr.random != null){
                curr.next.random = curr.random.next;
            }
            curr = curr.next.next;
        }

        // 3. Separate original list with copied one

        curr = head;
        Node currCopy = head.next;
        Node head2 = head.next;

        while(curr != null){
            curr.next = curr.next.next;
            if(currCopy.next != null){
                currCopy.next = currCopy.next.next;
            }
            curr = curr.next;
            currCopy = currCopy.next;
        }

        return head2;

    }
}


// #Pointers    Time Complexity: O(n) Space Complexity: O(1)
// 1. Create a deep copy of given list
// 2. allocate the random pointers to new list
// 3. Separate the original list from copied 