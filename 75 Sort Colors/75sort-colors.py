class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        id = 0 # Master pointer (iteration)
        l = 0 # takes care of 0's
        r = len(nums) - 1 # takes care of 2's

        while id <= r:

            if nums[id] == 0:
                nums[id], nums[l] = nums[l], nums[id]
                l+= 1
                id+=1
            
            elif nums[id] == 1:
                id+=1
            
            else : #nums[id] == 2
                nums[id], nums[r] = nums[r], nums[id]
                r-=1

            # print(nums)
        
