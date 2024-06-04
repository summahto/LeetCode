class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        lo = 0
        hi = sum(candies)// k

        def totalPiles(num):
            total = 0
            
            if num == 0 :
                return 0
            
            for c in candies:
                total += ( c // num)

            return total

        
        while lo < hi:
            
            mid = (lo + hi + 1) // 2
            
            if  totalPiles(mid) < k:
                hi = mid -1
            else :
                lo = mid

        return lo