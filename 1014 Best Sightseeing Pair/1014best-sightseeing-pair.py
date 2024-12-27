class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        n = len(values)
        maxSoFar = values[0] + 0
        ans = 0
        
        for i in range(1, n):
            
            ans = max(ans, maxSoFar + values[i] - i)
            maxSoFar = max(maxSoFar, values[i] + i)

        return ans
            