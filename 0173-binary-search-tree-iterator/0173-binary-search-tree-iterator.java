/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class ListNode{
    int val;
    ListNode next;

    public ListNode(int val, ListNode next){
        this.val = val;
        this.next = next;
    }

 }

class BSTIterator {
    ListNode head;
    ListNode dummy;
    public BSTIterator(TreeNode root) {
        head = new ListNode(-1,null);
        dummy = head;
        createLinkedList(root);        
    }
    
    public int next() {
        head = head.next;
        return head.val;
    }
    
    public boolean hasNext() {
        if(head.next != null) return true;

        return false;
    }

    private void createLinkedList(TreeNode root){
        //base
        if(root == null){
            return;
        }

        createLinkedList(root.left);
        ListNode node = new ListNode(root.val, null);
        dummy.next = node;
        // System.out.println(dummy.val + "before");
        dummy = dummy.next;
        // System.out.println(dummy.val + "after");
        createLinkedList(root.right);
    }
}
//Time Complexity: O(n)
// Space Complexity: O(n)
/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */