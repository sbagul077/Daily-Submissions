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
    public TreeNode balanceBST(TreeNode root) {
        List<Integer> inorder = new ArrayList<>();

        dfs(root, inorder);
        return createBalancedTree(inorder, 0, inorder.size()- 1);
    }


    private void dfs(TreeNode root, List<Integer> inorder){
        if(root == null){
            return;
        }

        dfs(root.left, inorder);
        inorder.add(root.val);
        dfs(root.right, inorder);
    }   


    private TreeNode createBalancedTree(List<Integer> inorder, int start, int end){
        //base
        if(start > end){
            return null;
        }

        int mid = start + (end - start) / 2;

        TreeNode left_subTree = createBalancedTree(inorder, start, mid - 1);
        TreeNode right_subTree = createBalancedTree(inorder, mid + 1, end);

        TreeNode node = new TreeNode(inorder.get(mid), left_subTree, right_subTree);
        // node.left = left_subTree;
        // node.right = right_subTree;

        return node;
    }
}

// Inorder Traversal + Recursive Construction
// Time Complexity: O(N)
// Space Complexity: O(N)