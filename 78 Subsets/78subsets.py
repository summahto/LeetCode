class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # powerSet = set()
        superlist = []
        self.backtrack(nums, superlist , 0, [])
        return superlist

    
    def backtrack(self, arr, superlist, index, curr):

        # print("curr", curr)
        # print("super", superlist)

        superlist.append(list(curr))
        # return

        for i in range(index, len(arr)):
            curr.append(arr[i])
            self.backtrack(arr, superlist, i+1, curr)
            curr.pop(-1)