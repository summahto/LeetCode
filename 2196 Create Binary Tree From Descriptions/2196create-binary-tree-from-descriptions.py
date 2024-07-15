# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        

        child_set = set()
        pMap = dict()
        # print(pMap)

        for desc in descriptions:
            if desc[0] not in pMap:
                pnode = TreeNode(desc[0])
                pMap[desc[0]] = pnode
            
            if desc[1] not in pMap:
                cnode = TreeNode(desc[1])
                pMap[desc[1]] = cnode
            
            child_set.add(desc[1])
            
            if desc[2] == 1:
                pMap[desc[0]].left = pMap[desc[1]]
            else :
                pMap[desc[0]].right = pMap[desc[1]]

        rootval = -1
        for desc in descriptions:
            if desc[0] not in child_set:
                rootval = desc[0]
                break

        # print(rootval)
        return pMap[rootval]