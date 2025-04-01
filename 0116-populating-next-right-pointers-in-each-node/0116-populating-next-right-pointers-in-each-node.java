/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/

class Solution {
    public Node connect(Node root) {
        if (root == null) {
            return null;
        }
        Queue<Node> q = new LinkedList<>();
        q.add(root);

        while (!q.isEmpty()) {
            int size = q.size();
            // System.out.println(size);
            Node currRoot = q.poll();
            // System.out.println(currRoot.val);

            if (currRoot.left != null) {
                q.add(currRoot.left);
            }
            if (currRoot.right != null) {
                q.add(currRoot.right);
            }
            for (int i = 1; i < size; i++) {
                Node temp = q.poll();

                currRoot.next = temp;
                currRoot = temp;
                if (currRoot.left != null) {
                    q.add(currRoot.left);
                }
                if (currRoot.right != null) {
                    q.add(currRoot.right);
                }
                // temp = currRoot;
            }
        }
        return root;
    }
}