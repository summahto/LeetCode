# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # dfs -> options LR
        def invert(l: Optional[TreeNode], r: Optional[TreeNode], level):
            if not l or not r:
                return
            
            if level & 1:
                l.val, r.val = r.val, l.val
            
            invert(l.left, r.right, level+1)
            invert(l.right, r.left, level+1)
        
        invert(root.left, root.right, 1)

        return root