class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        n = len(nums)

        bags = n + maxOperations
        total = sum(nums)

        lo = 1
        hi = max(nums)
        
        def check(maxBalls):
            reqOps = 0
            # Cannot do the average of the total because I dont have teh ability to re-distribute all the balls, rather I can only split balls in the bag into 2
            # avail = total
            # reqBags = ceil(avail/balls)

            # get the total number of required operations for all the balls
            # you can only split the balls into 2 bags
            for numBalls in nums:
                reqOps += ceil(numBalls/maxBalls) -1

            return reqOps
            

        while lo < hi:

            # print(f"{lo=} {hi=}")
            mid = (lo + hi) // 2

            # print(f"{check(mid)= }")

            # if reqOps is less than or equal to maxOps, that means we can further do more ops and add further more bags => reduction in number of balls
            if check(mid) <= maxOperations:
                hi = mid
            else :
                lo = mid + 1
            
        return lo