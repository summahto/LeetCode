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
        if(root == null)
            return root;
        
        Queue<Node> queue = new LinkedList<Node>();
        queue.add(root);
        doBFS(queue);
        return root;
        
    }
    
    public void doBFS(Queue<Node> q){
        
        while(!q.isEmpty()){
            int s = q.size();
            Node curr = null;
            
            for(int i=0; i<s; i++){
                Node prev = curr;
                curr = q.poll();
                
                if(prev != null)
                    prev.next = curr;
                    
                if(curr.left!= null)
                    q.add(curr.left);
                if(curr.right != null)
                    q.add(curr.right);
            }
            
        }
        
    }
}