# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root == None:
            return []

        pq = deque()
        pq.append(root)

        ans = []

        level = 0
        while pq:

            n = len(pq)
            # print(f"{n=}")

            levelNodes = []
            while n >0:
                # even level: pop the elements from left
                # push the elements to the back
            
                if level % 2 == 0:
                    curr = pq.popleft()

                    if curr.left:
                        pq.append(curr.left)
                    if curr.right:
                        pq.append(curr.right)
                
                # odd level pop the elements from the right
                # push the elements in the front
                else:
                    curr = pq.pop()
                    if curr.right:
                        pq.appendleft(curr.right)
                    if curr.left:
                        pq.appendleft(curr.left)
                
                levelNodes.append(curr.val)
                n -= 1
            
            ans.append(levelNodes)
            level += 1
            
            # print(ans)
        return ans


