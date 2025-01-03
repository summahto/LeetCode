class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        n = len(coins)        
        # pq =[]
        ans = [float("inf")]
        memo = {}

        coins.sort(reverse= True)
        # returns the minimum number of coins required for reaching to amount
        def dfs(i, a, count) :
            
            if (i,a) in memo and memo[(i, a)] <= count:
                return
                
            if i == n:
                # tried all the coins, return an invalid value
                return

            # print(f"{coins[i]=} {a=}")
            if a < 0:
                return

            if a == 0:
                # heapq.heappush(pq, count)
                ans[0] = min(ans[0], count)
                return
            

            memo[(i, a)] = count

            # take the current coin
            dfs(i, a - coins[i], count+1)
            # not take the current coin
            dfs(i+1, a, count)


        dfs(0, amount, 0)
        # print(f"{pq}")

        if ans[0] == float("inf"):
            return -1
        
        return ans[0]