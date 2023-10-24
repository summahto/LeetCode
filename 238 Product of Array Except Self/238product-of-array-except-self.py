class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
                
        curr = 1
        n = len(nums)
        ans = [1] * n
        for i in range(n):
            ans[i] *= curr
            curr *= nums[i]
            
        curr = 1

        i = n-1
        while i >= 0:
            ans[i] *= curr
            curr = curr* nums[i]
            i = i-1

        return ans