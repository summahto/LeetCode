/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {

        if(head == null || head.next == null)
            return null;
            

        ListNode slow = head, fast = head;
        Boolean isCycle = false;
        // int i = 1; YOU CAN SKIP i if you move slow and fast pointer before checkong the equality between them
        while(fast != null && fast.next != null){

            slow = slow.next;
            fast = fast.next.next;
            
            if(slow.equals(fast)){
                slow = head;
                while(!slow.equals(fast)){
                    slow = slow.next;
                    fast = fast.next; 
                }
                
                if(slow.equals(fast))
                    return slow;
            }


        }
        // System.out.println("slow " + slow + " :: Fast "  + fast + " , slow value " + slow.val + " Fast value " + fast.val);

        return null;

    }
}