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
    public List<Integer> rightSideView(TreeNode root) {
        
        List<Integer> res = new ArrayList<>();
        if(root == null)
            return res;
        
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        return doBFS(queue, res);
        
    }
    
    public List<Integer> doBFS(Queue<TreeNode> q, List<Integer> res){
        
        while(!q.isEmpty()){
            
            int s = q.size();
            for(int i=0; i< s ; i++){
                TreeNode curr = q.poll();
                if(i == s-1)
                    res.add(curr.val);
                
                if(curr.left != null)
                    q.add(curr.left);
                if(curr.right != null)
                    q.add(curr.right);
            }
        }
        
        return res;
    }
}