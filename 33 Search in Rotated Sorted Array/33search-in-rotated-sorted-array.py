class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        n = len(nums)
        lo, hi = 0, n-1

        while lo < hi:

            mid = (lo + hi) // 2

            if nums[mid] > nums[hi]:
                lo = mid + 1
            else :
                hi = mid
        
        l = lo
        r = n -1 + lo

        while l < r:

            mid = (l + r) // 2
            if nums[mid%n] < target :
                l = mid +1
            else :
                r = mid

        if nums[l%n] == target:
            return l%n
        
        return -1
