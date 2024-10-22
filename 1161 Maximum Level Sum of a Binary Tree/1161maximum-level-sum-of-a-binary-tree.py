# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        levelSum = 0
        level = 0
        maxSum = float('-inf')
        maxLevel = 1
        q = deque()
        q.append(root)

        while q:
            
            n = len(q)
            level+=1
            while n > 0:

                curr = q.popleft()
                levelSum += curr.val
                
                if curr.left:
                    q.append(curr.left)

                if curr.right:
                    q.append(curr.right)
            
                n-=1
            
            
            if levelSum > maxSum:
                maxSum = levelSum
                maxLevel = level
            
            # print(maxSum, levelSum)
            levelSum = 0
            
        
        return maxLevel


