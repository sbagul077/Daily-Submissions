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
    public List<Integer> largestValues(TreeNode root) {
        if(root == null){
            return new ArrayList<Integer>();
        }
        
        List<Integer> result = new ArrayList<Integer>();
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        
        while (!q.isEmpty()){
            int row_max = Integer.MIN_VALUE;
            int size = q.size();
            
            for(int i = 0; i < size; i++){
                TreeNode curr = q.remove();
                row_max = Math.max(row_max, curr.val);
                
                if(curr.left != null){
                    q.add(curr.left);
                }
                
                if(curr.right != null){
                    q.add(curr.right);
                }
            }
            result.add(row_max);
                
        }
        
        return result;
    }
}


//BFS
//Time Complexity: O(n)
// Space Complexity: O(n)