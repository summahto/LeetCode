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
    public int goodNodes(TreeNode root) {
        
        return totalGoodNodes(root, -10000);
    }

    public int totalGoodNodes(TreeNode root, int max){

        if(root == null)
            return 0;
        
        //result needs to be a local variable because we are calculating
        //result for each node
        int result = (root.val >= max) ? 1 : 0;

        // System.out.println(root.val + " : " + result );

        result += totalGoodNodes(root.left, Math.max(root.val, max));
        result += totalGoodNodes(root.right, Math.max(root.val, max));

        return result;
    }
}