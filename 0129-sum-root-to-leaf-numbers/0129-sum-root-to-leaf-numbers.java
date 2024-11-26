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
    public int sumNumbers(TreeNode root) {
        Stack<TreeNode> st = new Stack<>();
        Stack<Integer> numst = new Stack<>();
        // int[] numst = new List<>();
        int result = 0;
        int num = 0;
        
        while(root != null|| !st.isEmpty()){
            while(root != null){
                st.push(root);
                num = num * 10 + root.val;
                numst.push(num);
                root = root.left;
            }
            
            root = st.pop();
            num = numst.pop();

            if(root.right == null && root.left == null){
                result = result + num;
            }
            
            root = root.right;
        }
        return result;
    }
}