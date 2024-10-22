# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        heap = []

        q = deque()
        q.append(root)

        level = 0

        while q:

            level += 1
            levelSum = 0
            n = len(q)

            while n > 0:
                curr = q.popleft()
                levelSum += curr.val

                if curr.left:
                    q.append(curr.left)
                
                if curr.right:
                    q.append(curr.right)

                n-=1
            
            if  len(heap) < k:
                heapq.heappush(heap, levelSum)

            else :
                if levelSum > heap[0] :
                    heapq.heappop(heap)
                    heapq.heappush(heap, levelSum)
        
        if level < k:
            return -1

        print(heap)

        return heap[0]

            


