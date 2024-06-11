class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        n = len(nums)
        lo, hi = 0, n-1

        while lo < hi:

            mid = (lo + hi)// 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else :
                hi = mid
        
        # print(lo)
        return nums[lo]
