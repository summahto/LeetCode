# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(-1, head)
        l = r = kNode = dummy
        c = dummy.next
        count = 0


        while r.next:
            count += 1
            r = r.next
            # print(f'count : {count}')
            # print(f'val : {r.val}')

            if count == k :
                temp = c.next
                c.next = r.next

                # print(c.next.val)
                kNode = c
                count -= 1

                while count > 0:
                    # print(count)
                    prev = c
                    c = temp
                    temp = c.next
                    c.next = prev
                    count -= 1
                
                l.next = c
                l = r = kNode
                c = kNode.next
        
        t = dummy.next
        # while t:
        #     print(t.val)
        #     t = t.next
    
        return dummy.next
        


