# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if root == None:
            return True
        
        
        lh = self.maxDepth(root.left)
        rh = self.maxDepth(root.right)
        # print ("lh", lh)
        # print ("rh", rh)

        return (abs(lh - rh) < 2) and self.isBalanced(root.left) and self.isBalanced(root.right)


    def maxDepth(self, root) :
        if root == None :
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        