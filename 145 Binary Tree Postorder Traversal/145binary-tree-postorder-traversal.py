# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        

        def postOrder(root, ans):
            if root == None:
                return

            postOrder(root.left, ans)
            postOrder(root.right, ans)
            ans.append(root.val)


        ans = list()
        postOrder(root, ans)

        return ans

        # def traverse(node):

        