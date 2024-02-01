class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        
        n = len(nums)
        nums.sort()
        # print(nums)
        res = []

        for i in range(2, n, 3):
            # print(sNums[i])
            if nums[i] - nums[i-2] <= k:
                res.append([nums[i-2], nums[i-1], nums[i]])
            else :
                return []

        return res