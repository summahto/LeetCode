# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        list = []
        
        if(root is None):
            return list

        self.bfs(root, list)
        return list

    
    def bfs(self, root, outer) :
        
        q = []
        q.append(root)

        while(len(q)):

            size = len(q)
            inner = []

            i = 0
            while (i < size) :
                node = q.pop(0)
                inner.append(node.val)

                # print(inner)

                if(node.left):
                    q.append(node.left)

                if(node.right):
                    q.append(node.right)
                
                i+=1
            
            # print(inner)
            outer.append(inner)
        
        return outer
                
