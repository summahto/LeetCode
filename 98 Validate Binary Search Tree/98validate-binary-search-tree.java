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
    public boolean isValidBST(TreeNode root) {

        if(root == null || (root.left == null && root.right == null))
            return true;
        
        return checkValidBST(root, Long.MIN_VALUE, Long.MAX_VALUE);

        
    }

    public boolean checkValidBST(TreeNode root, long lb, long ub){

        if(root == null)
            return true;
        
        // System.out.println("lb " + lb + " val " + root.val + " ub " + ub);
        
        // if(root.val == Integer.MIN_VALUE && lb == Integer.MIN_VALUE)
        //     return true ;
            // && checkValidBST(root.left, lb, lb) && checkValidBST(root.right, root.val, ub);

        // if (root.val == Integer.MAX_VALUE && ub == Integer.MAX_VALUE)
        //     return true;
            // checkValidBST(root.left, lb, ub) && checkValidBST(root.right, lb, ub);

        if ((root.val <= lb || root.val >= ub))
            return false;

        return checkValidBST(root.left, lb, root.val) && checkValidBST(root.right, root.val, ub);
        


    }


}