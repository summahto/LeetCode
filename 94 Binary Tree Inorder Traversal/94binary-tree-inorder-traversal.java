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
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> inList = new ArrayList<Integer>();
        
        if(root == null)
            return inList;
        
        traverse(root, inList);
        return inList;
    }
    
    public void traverse(TreeNode root, List<Integer> inList){
        
        if(root.left != null){
            traverse(root.left, inList);
        }

        inList.add(root.val);

        if(root.right != null){
            traverse(root.right, inList);
        }
    }
}