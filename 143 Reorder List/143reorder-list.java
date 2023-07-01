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
    public void reorderList(ListNode head) {
        
        //starting with fast from 2nd node because this leads to slow always ending at the middle node
        ListNode slow = head, fast = head.next, pSlow = null;

        while(fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;

        }

        
        ListNode mid = slow;
        
        //slow is the starting of the 2nd half
        slow = slow.next;

        // breaking the 1st and 2nd half. First half containg the mid
        mid.next = null;

        // using a stack to reverse the 2nd half
        Deque<ListNode> stack = new LinkedList<>();
        while(slow != null){
            stack.push(slow);
            slow = slow.next;
        }


        // if i is odd i.e.  we have to add a no. from stack else add from the 1st list itself
        int i = 1; 
        ListNode nxt = head.next, curr = head, removed = null;

        while(!stack.isEmpty()){

            if(i % 2 != 0){

                removed = stack.pop();
                removed.next = null;
                curr.next = removed;

            } else {
                curr.next = nxt;
                nxt = nxt.next;
            }

            curr = curr.next;
            i++;
        }

        curr.next = nxt;
    }
}