# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        
        # nodes -> 1 to n but n's value is unknown
        # use cosntraints of the problem
        # indices => node value
        level = [-1]* 100001 # to find the level of the deleted Node
        height = [-1]* 100001 # Store the height of each node, pick the max after removing the deleted node
        maxHeightAtLevel = [0] * 100001 
        secMaxHeightAtLevel = [0] * 100001

        # Thought process:
        # when you delete a node, then on the same level get the max height remaining nodes
        # Use the maxheight in tandem with the level to get height of tree in O(1)
        # htAfterRemovingNode = L + H - 1

        # Using recursion I know how to get the height of the tree
        # modify the code to store height of each node
        # How to store the level of each node ??? -> pass another parameter level to the recursive function

        def setHeightLevel(root, lev):

            if not root:
                return 0


            level[root.val] = lev
            height[root.val] = max(setHeightLevel(root.left, lev+1), setHeightLevel(root.right, lev+1)) +1


            if height[root.val] > maxHeightAtLevel[lev]:
                secMaxHeightAtLevel[lev] = maxHeightAtLevel[lev]
                maxHeightAtLevel[lev] = height[root.val]
            
            elif height[root.val] > secMaxHeightAtLevel[lev]:
                secMaxHeightAtLevel[lev] = height[root.val]
            

            return height[root.val]

        setHeightLevel(root, 0)

        # print(f"{level=}")
        # print(f"{height=}")
        # print(f"{maxHeightAtLevel=}")
        # print(f"{secMaxHeightAtLevel=}")

        m = len(queries)

        ans =[]
        for val in queries:
            # how to delete node with value i in the tree
            
            currLevel = level[val]
            # get maxHeight at this level
            maxH = maxHeightAtLevel[currLevel]

            if height[val] == maxH:
                maxH = secMaxHeightAtLevel[currLevel]
                        
            ans.append( currLevel + maxH - 1)
        
        return ans
            






