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
    public ListNode mergeTwoLists(ListNode h1, ListNode h2) {

        if(h1 == null && h2 == null)
            return null;
        if(h1 == null)
            return h2;
        if(h2 == null)
            return h1;

        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;

        while(h1 != null && h2 != null){

            if(h1.val <= h2.val){
                curr.next = h1;
                h1 = h1.next;

            } else {
                curr.next = h2;
                h2 = h2.next;
            }

            curr = curr.next;
        }

        if(h1 != null)
            curr.next = h1;
        
        if(h2 != null)
            curr.next = h2;

        return dummy.next;

    }
}