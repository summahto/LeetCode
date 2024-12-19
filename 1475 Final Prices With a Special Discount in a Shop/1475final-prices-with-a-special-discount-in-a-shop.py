class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        n = len(prices)
        ans = prices
        stack = []
        i = 0

        while i < n:

            while stack and prices[i] <= prices[stack[-1]] :
                index = stack.pop()
                ans[index] -= prices[i]
            
            stack.append(i)
            i+= 1 
        
        return ans