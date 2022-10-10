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
    public List<Integer> preorderTraversal(TreeNode root) {
        
        List<Integer> elements = new ArrayList<>();
        
        if(root == null)
            return elements;
        
        TreeNode curr = root;
        
        preorder(curr, elements);
        
        return elements;
    }
    
    public void preorder(TreeNode curr, List<Integer> elements){
        
        elements.add(curr.val);
        
        if(curr.left != null)
            preorder(curr.left, elements );
        
        if(curr.right != null)
            preorder(curr.right, elements);
    }
}