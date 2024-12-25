# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
            
        q = deque()

        q.append(root)
        level = -1
        ans = []
        while q:
            level += 1

            n = len(q)
            levelMax = float('-inf')

            while n > 0:
                
                curr = q.popleft()
                levelMax = max(levelMax, curr.val)

                if curr.left:
                    q.append(curr.left)

                if curr.right:
                    q.append(curr.right)
                
                n -=1 
            
            ans.append(levelMax)

        return ans
            
