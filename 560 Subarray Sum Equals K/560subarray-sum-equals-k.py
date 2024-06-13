class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        preSum, count = 0, 0
        i = 0
        
        sumCount = defaultdict(int)
        sumCount[0] = 1

        for i in range(n):
            preSum+= nums[i]

            if sumCount[preSum - k] > 0:
                count+= sumCount[preSum - k]
            
            sumCount[preSum]+= 1

        return count
