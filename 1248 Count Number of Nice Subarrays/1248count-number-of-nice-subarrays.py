class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        i, j = 0, 0
        # oddCount = 0
        total = 0
        sum = 0
        sumCount = defaultdict(int)
        sumCount[0] = 1

        for i in range(n):
            nums[i] %= 2
            sum += nums[i]
            
            if sumCount[sum - k] > 0:
                total += sumCount[sum - k]
            
            sumCount[sum] += 1
            

        # for i in range(n):
        #     sum += nums[i]

        #     if sumCount[sum - k] > 0:
        #         total += sumCount[sum - k]
            
        #     sumCount[sum] += 1


        return total
