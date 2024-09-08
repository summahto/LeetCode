# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        # if at any path root is null return false
        if root is None:
            return False

        # check at the root
        # but then call isSubPath because we need to if root's left or right subtree have the path
        # isSubPath is required because it calls child of child as well for various roots
        return self.isPresent(root, head) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

        
    def isPresent(self, root, tempHead) -> bool:
        
        if tempHead == None:
            return True

        if root == None:
            return False

        # if at any moment the values are unequal return false, but this is only for one of the paths
        if root.val != tempHead.val:
            return False
        
        
        return self.isPresent(root.left, tempHead.next) or self.isPresent(root.right, tempHead.next)