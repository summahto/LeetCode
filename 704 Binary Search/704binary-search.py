class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        lo, hi = 0, len(nums)

        while lo < hi :
            mid = (lo + hi) // 2 

            if nums[mid] < target:
                lo = mid + 1
            else :
                hi = mid

        
        if lo == len(nums) or nums[lo] != target :
            return -1

        return lo