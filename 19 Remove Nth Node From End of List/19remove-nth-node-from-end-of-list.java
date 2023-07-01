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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        
        ListNode start = new ListNode(0);
        start.next= head;

        ListNode slow = start, fast = start;

        int i = 0;
        //this will go n spaces
        while(i < n+1){
            fast = fast.next;
            i++;
        }

        //this will take 2(l-n) spaces
        while(fast != null){
            fast = fast.next;
            slow = slow.next;
        }

        ListNode temp = slow.next.next;
        slow.next = temp;


        return start.next;
        
    }
}