class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 3:
            return nums[0] + nums[1] + nums[2]
        
        minCost = float("inf")
        
        for j in range(1, n-1):
            cost = nums[j]

            for k in range(j+1, n):
                cost += nums[k]
                minCost = min(cost, minCost) 
                cost = nums[j]
        
        return nums[0] + minCost                  
            
                
            
        