/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        Node curr = head ;

        Map<Node, Node> nodeMap = new HashMap<>();

        while(curr != null){
            nodeMap.put(curr, new Node(curr.val));
            curr = curr.next;
        }

        curr = head;
        while(curr != null){

            nodeMap.get(curr).next = nodeMap.get(curr.next);
            nodeMap.get(curr).random = nodeMap.get(curr.random); 

            curr = curr.next;
        }

        return nodeMap.get(head);
    }

    
}