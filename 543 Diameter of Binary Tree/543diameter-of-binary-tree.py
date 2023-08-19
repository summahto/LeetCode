# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    maxD = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.maxDepth(root)
        return self.maxD
        

    def maxDepth(self, root):
        if(root == None):
            return 0
        
        lh = self.maxDepth(root.left)
        rh = self.maxDepth(root.right)

        self.maxD = max(self.maxD, lh + rh)

        return 1 + max(lh, rh)

    

        