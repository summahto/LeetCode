# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if(root == None):
            return False
        
        if(self.isSubRoot(root, subRoot)):
            return True
        else :
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    
    def isSubRoot(self, root, subRoot):

        if(root == None and subRoot == None):
            return True
        elif(root != None and subRoot == None):
            return False
        elif(root == None and subRoot != None):
            return False
        else :
            if(root.val == subRoot.val):
                return self.isSubRoot(root.left, subRoot.left) and self.isSubRoot(root.right, subRoot.right)
            else :
                return False
        


        
        