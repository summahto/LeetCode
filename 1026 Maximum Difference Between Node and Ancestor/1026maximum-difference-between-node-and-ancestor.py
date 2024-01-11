# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        

        def findMaxDiffInSubtree(rootVal, root, maxDiff) :

            if root.left == None and root.right == None:
                return maxDiff[0]
            
            if root.left != None:
                findMaxDiffInSubtree(rootVal, root.left, maxDiff)
                diff = abs(rootVal - root.left.val)
                maxDiff[0] = max(diff, maxDiff[0])
                # print("inside left subtree", root.left.val, diff, maxDiff)

            if root.right != None:
                findMaxDiffInSubtree(rootVal, root.right, maxDiff)
                diff = abs(rootVal - root.right.val)
                maxDiff[0] = max(diff, maxDiff[0])
                # print("inside right subtree", root.right.val, diff, maxDiff)
            
            return maxDiff[0]



        
        def traverse(node, currDiff):
            if node == None:
                return
            
            currDiff[0] = max(findMaxDiffInSubtree(node.val, node, currDiff), currDiff[0])
            traverse(node.left, currDiff)
            traverse(node.right, currDiff)

            return currDiff[0]

            
            

        diff = [0]
        maximum = traverse(root, diff)

        return maximum

        

        