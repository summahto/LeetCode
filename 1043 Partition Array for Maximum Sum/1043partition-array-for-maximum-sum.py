class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        def solve(i, memo):

            if i == len(arr):
                return 0

            if i in memo:
                return memo[i]

            cMax = -1
            result = 0
            for x in range(0,k):
                
                if i+x < len(arr):
                    
                    cMax = max(cMax, arr[i+x])
                    result = max(result, (cMax * (x+1)) + solve(i+x+1, memo))
                    # print(result)

            memo[i] = result        
            return result

        memo = {}
        return solve(0, memo)

