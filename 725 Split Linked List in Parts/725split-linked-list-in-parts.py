# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        

        length : int = 0

        curr = head

        while curr is not None:
            length += 1

            curr = curr.next
        
        ans = []
        curr = head
        if k >= length:
            # more parts are required than available
            while curr is not None:
                nxt = curr.next

                curr.next = None
                ans.append(curr)
                k -= 1
                curr = nxt
            
            while k > 0:
                ans.append(None)
                k -= 1
        
        else :
            # dummy = ListNode( -1, head)
            # curr = dummy
            q = length//k  # total parts
            r = length %k  # extra parts
            
            totalParts = k
            # while curr is not None:
                
            while totalParts > 0:
                
                partLength = q
                
                if r > 0:
                    partLength += 1
                    r -=  1
                
                # print("TP : ", totalParts)
                start = curr
                while partLength > 1:
                    # print(partLength, curr.val)

                    partLength -= 1
                    curr = curr.next

                nxt = curr.next
                curr.next = None

                curr = nxt
                totalParts -= 1

                ans.append(start)
                # print(ans)

        return ans