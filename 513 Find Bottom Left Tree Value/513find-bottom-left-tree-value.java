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
    public int findBottomLeftValue(TreeNode root) {
        
        if(root == null)
            return 0;
        else if(root.left == null && root.right == null)
            return root.val;
        
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        return doBFS(queue);
    }
    
    public int doBFS (Queue<TreeNode> q) {
        int leftLast = 0;
        
            while(!q.isEmpty()){
            
            TreeNode curr = null;
            int s = q.size();
            leftLast = q.peek().val;
                
            for(int i=0; i< s ; i++){
                curr = q.poll();
                
                if(curr.left != null){
                    q.add(curr.left);
                }
                    
                if(curr.right != null)
                    q.add(curr.right);
            }
                
        }
        return leftLast;
    }
}