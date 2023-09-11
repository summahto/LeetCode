class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        superlist = []
        self.backtrack(nums, superlist, [])

        return superlist


    def backtrack(self, nums, superlist, curr):
        
        # print("curr", curr)
        # print("superlist", superlist)

        if(len(curr) == len(nums)) :
            superlist.append(list(curr))
            return

        for i in range(0, len(nums)):

            if(nums[i] not in curr):
                curr.append(nums[i])
                self.backtrack(nums, superlist, curr)
                curr.pop(-1)
