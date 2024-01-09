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
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {

        List<Integer> l1 = new ArrayList<>();
        leafNodes(root1, l1);
        
        List<Integer> l2 = new ArrayList<>();
        leafNodes(root2, l2);

        return l1.equals(l2);

        // if(l1.size() != l2.size()) return false;
        // else {
            
        // }
        
    }

    public void leafNodes(TreeNode root, List<Integer> l){
        
        if(root.left == null && root.right == null)
            l.add(root.val);
        
        if(root.left != null)
            leafNodes(root.left, l);
        
        if(root.right != null)
            leafNodes(root.right, l);

    }
}