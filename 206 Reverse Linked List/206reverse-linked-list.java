/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {

        if (head == null)
            return null;
        if(head.next == null)
            return head;
        
        ListNode curr = head, prev = null, nxt = curr.next;
        while(nxt != null){
            curr.next = prev;
            prev = curr;
            curr = nxt;
            nxt = nxt.next;
        }

        curr.next = prev;

        return curr;

    }
}