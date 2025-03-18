/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    List<TreeNode> pathP;
    List<TreeNode> pathQ;
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(root == null || root == p || root == q){
            return root;
        }

        this.pathP = new ArrayList<>();
        this.pathQ = new ArrayList<>();

        backtrack(root, p, q, new ArrayList<>());
        //we can iterate on both paths

        for(int i = 0; i < pathP.size(); i++){
            if(pathP.get(i).val != pathQ.get(i).val){
                return pathP.get(i - 1);
            }
        }
        return null;
    }

    private void backtrack(TreeNode root, TreeNode p, TreeNode q, List<TreeNode> path){
        //base case
        if(root == null){
            return;
        }
        //logic
        if(root.val == p.val){
            path.add(p);
            path.add(p);
            pathP = new ArrayList<>(path);
            path.remove(path.size() - 1);
            path.remove(path.size() - 1);
        }

        if(root.val == q.val){
            path.add(q);
            path.add(q);
            pathQ = new ArrayList<>(path);
            path.remove(path.size() - 1);
            path.remove(path.size() - 1);
        }

        //action 
        path.add(root);
        backtrack(root.left, p, q, path);
        backtrack(root.right, p, q, path);
        //backtrack
        path.remove(path.size() - 1);
    }
}