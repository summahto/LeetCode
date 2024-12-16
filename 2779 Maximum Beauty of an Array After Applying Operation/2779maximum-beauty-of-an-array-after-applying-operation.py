class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        
        i, j = 0, 0

        n = len(nums)
        # Since this is asking for a subsequence order of the numbers does not matter
        nums.sort()

        maxLen = 1

        while j < n:
            
            while nums[j] > nums[i] + 2*k:
                i+= 1
            
            maxLen = max(maxLen, j-i+1)
            j+=1
        
        return maxLen
