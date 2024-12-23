# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        
        q = deque()
        q.append(root)


        # level = -1
        numSwaps = 0
        while q:
            
            n = len(q)
            levelNums = []

            numIndexMap = dict()
            i = 0
            while n > 0:

                curr = q.popleft()

                levelNums.append(curr.val)
                numIndexMap[curr.val] = i

                if curr.left:
                    q.append(curr.left)
                
                if curr.right:
                    q.append(curr.right)

                n -=1
                i += 1

            sortedNums = sorted(levelNums)
            
            for i in range(len(levelNums)):
                
                if levelNums[i]  != sortedNums[i]:
                    idx= numIndexMap[sortedNums[i]]
                    
                    levelNums[i], levelNums[idx] = levelNums[idx], levelNums[i]

                    # update the index in map
                    numIndexMap[levelNums[i]] = i
                    numIndexMap[levelNums[idx]] = idx
                    numSwaps += 1


                # print(f'{i=} {correctPos=} {levelNums[i]=} {sortedNums[correctPos]}')

            # print(f'{sortedNums=} {levelNums=}')
        return numSwaps


        
