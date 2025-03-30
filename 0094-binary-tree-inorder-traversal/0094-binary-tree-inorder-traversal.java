class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<Integer>();
        if(root == null){
            return new ArrayList<> ();
        }
        helper(root, result);
        return result;
    }

    private void helper(TreeNode root,  List<Integer> result ){
        if(root == null){
            return;
        }
        System.out.print(" "); 
        System.out.print("Up"); 
        System.out.print(root.val);
        helper(root.left, result);
        result.add(root.val);
        helper(root.right, result);
    }
}