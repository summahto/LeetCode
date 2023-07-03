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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        
        if(l1 == null && l2 == null)
            return null;
        if(l1 == null)
            return l2;
        if(l2 == null)
            return l1;
        
        ListNode start = new ListNode(0);
        ListNode curr = start;

        int carry = 0, val = 0, sum = 0;
        while(l1 != null && l2 != null){
            
            sum = l1.val + l2.val + carry;
            if(sum >= 10){
                val = sum % 10;
                carry = sum/ 10;
            } else {
                val = sum;
                carry = 0;
            }

            ListNode nxt = new ListNode(val);
            curr.next = nxt;

            l1 = l1.next;
            l2 = l2.next;
            curr = curr.next;

        }

        while(l1 != null){
            sum = l1.val + carry;
            
            if(sum >= 10){
                val = sum % 10;
                carry = sum/10;
            } else {
                val = sum;
                carry = 0;
            }

            ListNode nxt = new ListNode(val);
            curr.next = nxt;

            l1 = l1.next;
            curr = curr.next;

        }

        while(l2 != null){
            sum = l2.val + carry;
            
            if(sum >= 10){
                val = sum % 10;
                carry = sum /10;
            } else {
                val = sum;
                carry = 0;
            }

            ListNode nxt = new ListNode(val);
            curr.next = nxt;

            l2 = l2.next;
            curr = curr.next;

        }

        if(carry > 0){
            ListNode nxt = new ListNode(carry);
            curr.next = nxt;
        }


        return start.next;

    }
}