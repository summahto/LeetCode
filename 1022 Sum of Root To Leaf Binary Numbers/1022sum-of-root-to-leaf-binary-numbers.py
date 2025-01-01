# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        # tot =0

        # def dfs(root, s):
        #     if not root:
        #         print(s, int(s, 2))
        #         return int(s, 2)
            
        #     s+= str(root.val)
        #     ans = 0

        #     ans += dfs(root.left, s)
        #     ans += dfs(root.right, s)

        #     return ans

        
        # return int(dfs(root, '')/2)
        # if root.left == None and root.right == None:


        def dfs(root, s):
            s += str(root.val)

            if root.left == None and root.right == None:
                # print(s, int(s,2))
                return int(s, 2)

            ans = 0
            if root.left:
                ans += dfs(root.left, s)
            
            if root.right:
                ans += dfs(root.right, s)

            return ans
            
        return dfs(root, '')
