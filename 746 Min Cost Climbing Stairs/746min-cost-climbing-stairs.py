class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)
        # memo = {}

        # bottom-up approach but with dp array
        # dp = [0]* n
        # dp[0] = cost[0]
        # dp[1] = cost[1]

        # bottom-up approach with constant space
        first = cost[0]
        second = cost[1]

        for i in range(2, n):
            currCost = cost[i] + min(first, second)
            first = second
            second = currCost

        # print(dp)

        return min(first, second)


        # we don't need to add the cost[n] for the nth step
        # return min(self.dp(cost, n-1, memo), self.dp(cost, n-2, memo))
        
    

        
