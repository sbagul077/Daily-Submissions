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
class Solution {
    TreeNode first;
    TreeNode second;
    TreeNode prev;
    boolean flag;
    public void recoverTree(TreeNode root) {
        if(root == null) return;
        inorder(root);

        int temp = first.val;
        first.val = second.val;
        second.val = temp;
    }

    private void inorder(TreeNode root){
        //base
        if(root == null){
            return;
        }
        //logic
        inorder(root.left);
        if(prev != null && prev.val >= root.val){
            if(!flag){
                first = prev;
                second = root;
                flag = true;
            }
            else{
                second = root;
            }
        }

        prev = root;
        inorder(root.right);
    }
}

//DFS
//Time Complexity: O(n)
//Space Complexity: O(n)
