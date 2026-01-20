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

    int result;
    public int sumNumbers(TreeNode root) {
        if(root == null){
            return 0;
        }

        return inorder(root, 0);
        // return result;
    }

    private int inorder(TreeNode root, Integer rootSum){
        //base
        if(root == null){
            return 0;
        }
        
        if(root.left == null && root.right == null){
            return  (rootSum * 10) + root.val;
        }

        //logic
        return inorder(root.left, rootSum * 10 + root.val) + inorder(root.right, rootSum * 10 + root.val);
    }
}