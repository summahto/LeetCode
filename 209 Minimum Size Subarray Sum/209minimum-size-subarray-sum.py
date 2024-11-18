class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)

        i, j = 0, 0
        total = 0
        min_len = n+1

        while j < n:

            total += nums[j]

            while total >= target:
                # reduce from the left and reduce the sum
                min_len = min(min_len, j-i+1)
                total -= nums[i]
                i+=1
            

            j += 1
        
        if min_len < n+1:
            return min_len
        
        return 0