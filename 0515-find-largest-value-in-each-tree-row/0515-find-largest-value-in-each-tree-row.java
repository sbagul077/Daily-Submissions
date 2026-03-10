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
    List<Integer> result;
    public List<Integer> largestValues(TreeNode root) {
        result = new ArrayList<>();

        if(root == null){
            return result;
        }

        helper(root, 1);

        return result;
    }

    private void helper(TreeNode root, Integer level){
        //base
        if(root == null){
            return;
        }

        if(level > result.size()){
            result.add(root.val);
        }

        if(level <= result.size()){
            if(result.get(level - 1) < root.val){
                result.set(level - 1, root.val);
            }            
        }

        helper(root.left, level + 1);
        helper(root.right, level + 1);
    }
}

// DFS
// Maintain level at each level and update the result at index when larger element is found
// Time Complexity: O(n)
// Space Complexity: O(h)
