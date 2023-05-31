class Solution:
    def mySqrt(self, x: int) -> int:

        l, r = 1, x
        while(l <= r):
            mid = l + (r-l) // 2

            if(mid * mid <= x):
                l = mid + 1
            else :
                r = mid -1
        
        return l - 1