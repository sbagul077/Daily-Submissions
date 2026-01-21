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
    List<List<Integer>> result;
    List<Integer> path;
    Integer target;
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        this.result = new ArrayList<>();
        this.path = new ArrayList<>();
        this.target = targetSum;
        
        helper(root, 0);

        return result;
    }

    private void helper(TreeNode root, int pathSum){
        //base
        if(root == null){
            return;
        }
        
        path.add(root.val);
        pathSum += root.val;


        if(root.left == null && root.right == null && target == pathSum){
            
            result.add(new ArrayList<>(path));
        }
        

        helper(root.left, pathSum);
   
        
        helper(root.right, pathSum);
        path.removeLast();

    }
}