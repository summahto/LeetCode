/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    public Node cloneGraph(Node node) {
        
        if(node == null)
            return null;
        if(node.neighbors == null || node.neighbors.size() == 0)
            return new Node(node.val);    

        // System.out.println(node.val);
        Node start = new Node(node.val);
        Queue<Pair<Node, Node>> q = new LinkedList<>();
        q.add(new Pair<>(node, start));
        Map<Node, Node> visited = new HashMap<>();
        visited.put(node, start);
        
        while(!q.isEmpty()) {
            Pair<Node, Node> p = q.poll();

            // System.out.println(p.getKey());
            Node oNode = p.getKey();
            Node cNode = p.getValue();
            List<Node> cNeighbors = new ArrayList<>();

            for(Node n: oNode.neighbors){
                if(!visited.containsKey(n)){
                    Node newNode = new Node(n.val);
                    cNeighbors.add(newNode);
                    q.add(new Pair(n, newNode));
                    visited.put(n, newNode);
                } else {
                    cNeighbors.add(visited.get(n));
                    // q.add(new Pair(n, visited.get()));
                }
            }

            cNode.neighbors = cNeighbors;
        }

        return start;
        // return null;
    }
}