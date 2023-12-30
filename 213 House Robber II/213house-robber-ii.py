class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)

        if n == 1:
            return nums[0]
        
        if n == 2:
            return max(nums[0], nums[1])

        f = [0] * (n-1)
        g = [0] * n

        f[0] = nums[0]
        f[1] = nums[0]
        # f[2] = max(nums[1], f[0])
        
        g[0] = 0
        g[1] = nums[1]
        # g[2] = max(nums[2] + g[0], g[1])


        for i in range(2, n-1):
            f[i] = max(nums[i] + f[i-2], f[i-1])

            # Not sure why I was trying to use this recurrence relationship when it was not at all in House Robber 1. 
            # I had to apply House Robber 1 in 2 different sets and find the maximum of the 2 (0... n-1) & (1... n)
            # f[i] = max(nums[i-1] + f[i-3], f[i-1]).
        
        for i in range(2, n):
            g[i] = max(nums[i] + g[i-2], g[i-1])

        # print(f)
        # print(g)

        return max(f[-1], g[-1])

        
        