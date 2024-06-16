class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        
        hi = max(nums)
        countMap = [0] * (hi + len(nums))

        for num in nums:
            countMap[num] += 1

        ans = 0
        i = 0
        for i in range(len(countMap)):
            
            if countMap[i] > 1:
                carry = countMap[i] - 1
                countMap[i+1] += carry
                ans += carry
            
            i+= 1
        return ans