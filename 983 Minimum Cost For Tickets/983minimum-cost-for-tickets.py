class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)

        # takes the index of the days array and returns the minumim cost
        def dfs(i, dp) -> int:
            
            if i == n:
                return 0

            if dp[i] != -1:
                return dp[i]

            # 3 options
            # take a 1daypass
            cost1DayPass = costs[0] + dfs(i+1, dp) 

            # take a 7 day pass
            j = bisect_left(days, days[i] + 7)
            cost7DayPass = costs[1] + dfs(j, dp)
            
            # take a 30 day pass
            k = bisect_left(days, days[i] +30)
            cost30DayPass = costs[2] + dfs(k, dp)
            
            dp[i] = min(cost1DayPass, cost7DayPass, cost30DayPass) 
            return dp[i]
            

        dp = [-1] * n
        return dfs(0, dp)