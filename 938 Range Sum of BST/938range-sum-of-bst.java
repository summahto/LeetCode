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
    public int rangeSumBST(TreeNode root, int low, int high) {
        
        TreeNode curr = root;
        
        int [] sum = new int[1];
        
        inorder(curr, low, high, sum);

        return sum[0];

    }

    public void inorder(TreeNode root, int low, int high, int [] sum){

        if(root == null)
            return;

        if(low < root.val)
            inorder(root.left, low, high, sum);

        if(root.val >= low && root.val <= high)
            sum[0] += root.val;

        if(high > root.val)
            inorder(root.right, low, high, sum);

        
    }
}