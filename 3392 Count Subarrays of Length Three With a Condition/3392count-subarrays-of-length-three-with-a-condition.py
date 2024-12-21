class Solution:
    def countSubarrays(self, nums: List[int]) -> int:

        n = len(nums)
        i, j = 0, 2

        s = 0
        count = 0
        while j < n:
            s = nums[i] + nums[j]
    
            if (nums[j-1]/2) == s:
                # print(nums[i] + nums[j], nums[j-1]//2)
                count += 1

            i+=1
            j+=1 

        return count