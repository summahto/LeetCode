class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        ans = 0
        def atMost(k):
            i, j = 0,0
            prefSum = 0
            count = 0

            while j< n:
                prefSum += nums[j]

                while prefSum > k and i <= j:
                    # count += 1
                    prefSum -= nums[i]
                    i += 1
                
                count += (j- i +1)
                

                j += 1

            return count
        
        ans = atMost(goal) - atMost(goal - 1)
        
        # ans = atMost(goal)
        return ans