class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        
        position.sort()
        lo = 1
        hi = (position[-1] - lo)// (m-1)


        def canPlaceBalls(d):
            ballsPlaced = 1
            prev = position[0]

            i = 1
            while i< len(position):
                
                curr = position[i]
                
                if curr - prev >= d:
                    ballsPlaced += 1
                    prev = curr
                
                # print(d, ballsPlaced)
                
                if ballsPlaced == m:
                    return True

                i+=1


            return False
        
        # ans = lo
        while lo < hi:
            # mid = (lo + (hi- lo) + 1)// 2
            mid = (lo + hi + 1)// 2

            if canPlaceBalls(mid):
                lo = mid
                # ans = mid
            else :
                hi = mid -1

        return lo