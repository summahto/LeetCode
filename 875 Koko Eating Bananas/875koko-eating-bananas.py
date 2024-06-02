class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        hi = max(piles)
        lo = 1

        def timeTaken(speed : int):
            
            # print("speed :" , speed)
            i = 0
            total = 0
            while i< len(piles):
                if piles[i] <= speed:
                    total += 1
                else : 
                    if piles[i] % speed == 0:
                        total += (piles[i] // speed)
                    else :
                        total += (piles[i] // speed) + 1

                
                i+=1
            
            # print("total :" ,total)
            return total

        while lo < hi:
            mid = (lo + hi )//2

            if timeTaken(mid) <= h:
                # we have more time => we can reduce the speed
                hi = mid
            else :
                # we have crossed the limit => increase the speed
                lo = mid +1
        
        return lo
        

            
