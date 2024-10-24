# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        q = deque()
        level = 0
        # parSumMap = defaultdict(list)
        q.append((root, -1))

        while q:
            n = len(q)
            level += 1
            levelSum = 0

            parSumMap = defaultdict(list)
            while n > 0:
                curr, parent = q.popleft()
                levelSum += curr.val

                if level <= 2:
                    curr.val = 0    
                else:
                    # level is > 3,
                    parSumMap[parent].append(curr.val) 

                if curr.left:
                    q.append((curr.left, curr))

                if curr.right:
                    q.append((curr.right, curr))
                n-=1
            
            if level >= 3:
                for parent in parSumMap:
                    otherCousinsSum = levelSum - sum(parSumMap[parent])
                    # print(parent.val, levelSum, level, sum(parSumMap[parent]))
                    if parent.left:
                        parent.left.val = otherCousinsSum
                    
                    if parent.right:
                        parent.right.val = otherCousinsSum
        
        return root
        