class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = []
        n = len(nums)
        ans.append(nums[0])

        for i in range(1, n):
            if nums[i] > ans[-1]:
                ans.append(nums[i])
            
            else :
                pos = bisect_left(ans, nums[i])
                ans[pos] = nums[i]

        # print(ans)
        return len(ans)

