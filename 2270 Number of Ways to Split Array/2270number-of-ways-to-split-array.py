class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        
        total = sum(nums)
        lsum, rsum = 0, total
        count =0
        for i in range(len(nums) -1):
            lsum += nums[i]
            rsum -= nums[i]

            if lsum >= rsum:
                count += 1
        return count