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

    int gmax = Integer.MIN_VALUE;

    public int maxPathSum(TreeNode root) {
        
        // Integer gsum = Integer.MIN_VALUE;

        maxPathSumHelper(root);

        return gmax;

    }

    public int maxPathSumHelper(TreeNode root){

        if(root == null)
            return 0;
        
        int leftMax = maxPathSumHelper(root.left);
        int rightMax = maxPathSumHelper(root.right);

        int maxLeftRight = Math.max(leftMax, rightMax);
        int maxSumRootAndLeftRight = Math.max(root.val, (root.val + maxLeftRight));
        int maxSumComplete = Math.max(maxSumRootAndLeftRight, (root.val + leftMax + rightMax));

        gmax = Math.max(gmax, maxSumComplete);

        return maxSumRootAndLeftRight;
    }
}