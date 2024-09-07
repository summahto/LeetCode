# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        

        uniq = set(nums)
        # dummy trick is important : REMEMBER THIS
        dummy = ListNode(next= head)
        curr = dummy

        while curr.next:
            if curr.next.val in uniq:
                curr.next = curr.next.next
            
            else :
                curr = curr.next
        
        return dummy.next



        # temp = head

        # TEST the final linked list
        # while temp != None:
        #     print(temp.val, "->", end= '')
        #     temp = temp.next
        
        

        # return head