# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        ans =[]
        dq= deque()

        dq.append(root)

        while dq:

            level = []
            n = len(dq)
            # print(f"{ans=} {n=}")

            while n > 0:
                curr = dq.popleft()
                level.append(curr.val)
                
                # print(f"{curr.val=}")
                
                if curr.left:
                    dq.append(curr.left)
                
                if curr.right:
                    dq.append(curr.right)

                n-= 1
            
            ans.append(level)

        
        # print(f"{ans=}")
        return ans[::-1]

