class Solution:
    def trap(self, height: List[int]) -> int:

        l, lmax, r, rmax = 0, 0, len(height) - 1, len(height) - 1
        total = 0
        while l <= r :

            if height[l] < height[r] :
                if height[lmax] < height[l] :
                    lmax = l
                else: 
                    total += height[lmax] - height[l]
                l+= 1


            else :
                if height[rmax] < height[r] :
                    rmax = r
                else :
                    total += height[rmax] - height[r]

                r-= 1


            
        return total

        