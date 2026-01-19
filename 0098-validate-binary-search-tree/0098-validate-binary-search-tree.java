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
    public boolean isValidBST(TreeNode root) {
        if(root == null){
            return true;
        }

        return helper(root, null, null);                
    }

    private boolean helper(TreeNode root, Integer min, Integer max){
        //base
        if(root == null){
            return true;
        }
        if(max != null && root.val >= max) return false;

        if(min != null && root.val <= min) return false;
        //logic

        // boolean case1 = ;

        // boolean case2 = ;

        return helper(root.left, min, root.val) & helper(root.right, root.val, max);
    }
}