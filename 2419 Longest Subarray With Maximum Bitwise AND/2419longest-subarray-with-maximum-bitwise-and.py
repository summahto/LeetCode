class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        max_value = 0
        streak = 0
        ans = 0

        for i in range(n):

            if nums[i] > max_value:
                max_value = nums[i]
                # mistake : new max found, its streak and answer should have been reset to 0 
                streak = 0
                ans = 0
        
            if nums[i] == max_value:
                streak += 1
            
            else :
                streak = 0
            
            ans = max(ans, streak)
                
            

        return ans
