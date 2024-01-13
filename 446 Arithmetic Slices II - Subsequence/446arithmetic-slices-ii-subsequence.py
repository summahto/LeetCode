class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        ans, n = 0, len(nums)
        # creates a dict for each index, defaultdict sets all the values to 0 and does not throw error if a key which is not present is accessed
        dp = [defaultdict(int) for i in range(n)]
        
        # we are looking for slices of length 2 or more, hence i starts from 1
        for i in range(1,n):
            
            for j in range(0,i):
                cd = nums[i] - nums[j]
                dp[i][cd] += dp[j][cd] + 1
                ans += dp[j][cd]


        # print(dp)

        # duplicate_permutations = n*(n-1)// 2
        
       # subtract the combinations of length 2 from ans
        return ans
        