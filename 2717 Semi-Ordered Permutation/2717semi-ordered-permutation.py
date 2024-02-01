class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        mini = float('inf')
        maxi = float('-inf')

        minIdx = 0
        maxIdx = 0
        # print(min, max)

        for i in range(n):

            if mini > nums[i]:
                mini = nums[i]
                minIdx = i

            if maxi < nums[i]:
                maxi = nums[i]
                maxIdx = i
        

        if minIdx > maxIdx:
            return (minIdx - 0) + (n-1 - maxIdx) -1
        else:
            return (minIdx - 0) + ((n-1) - maxIdx)
         