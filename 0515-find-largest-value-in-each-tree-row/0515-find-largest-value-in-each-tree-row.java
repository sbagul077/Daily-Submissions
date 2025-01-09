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
        List<Integer> result = new ArrayList<>();
        if(root == null){
            return result;
        }

        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);

        while(!q.isEmpty()){
            int size = q.size();
            int max = Integer.MIN_VALUE;

            for(int i = 0; i < size; i++){
                TreeNode currRoot = q.poll();

                if(max < currRoot.val){
                    max = currRoot.val;
                }

                if(currRoot.left != null){
                    q.add(currRoot.left);
                }

                if(currRoot.right != null){
                    q.add(currRoot.right);
                }
            }
            result.add(max);
            
        }
        return result;

    }
}