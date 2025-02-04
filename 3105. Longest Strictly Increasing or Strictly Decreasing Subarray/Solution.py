class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        # I was thinking in terms of tracking what was the state before and what is the state now
        # state stands for whether I saw -> previously was it increasing/decreasing or the same.
        # Think in terms of what you need to track 
        # here, I only need to track 2 lengths and both of them can either increase or get reset
        # The problem was : my mind is trained to keep track of only 1 length i.e. curr length
        # never thought of having multiple lengths. if there are finite lengths(2 here) which you can track
        # then why not track both of them
        n = len(nums)
        incLength = decLength = maxLength = 1

        for i in range(1, n):
            if nums[i] > nums[i-1]:
                incLength += 1
                decLength = 1
            elif nums[i] < nums[i-1]:
                decLength += 1
                incLength = 1
            else:
                incLength = 1
                decLength = 1
            
            maxLength = max(incLength, decLength, maxLength)

        return maxLength
