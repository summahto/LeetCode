class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # currSum = 0

        total = sum(nums)
        if total < target or total < (-1)* target:
            return 0

        def recurse(i, currSum, dp) -> int:

            # when you reach the end of the array, and running sum == target => one of the ways
            if i == n and currSum == target:
                return 1
            
            if i == n :
                return 0
            
            if dp[i][currSum] is not None:
                return dp[i][currSum]
            
            dp[i][currSum] = recurse(i+1, currSum - nums[i], dp) + recurse(i+1, currSum + nums[i], dp)
            
            return dp[i][currSum]

        # how to initialize 2d dictionary for memoization ? 
        dp = defaultdict(lambda: defaultdict(lambda: None))
        # dp = {None for }
        ans = recurse(0, 0, dp)

        return ans