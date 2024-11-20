class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        i, j = 0, 0

        curr_window = set()
        total = 0
        max_sum = 0
        while j < n:

            while nums[j] in curr_window:
                total -= nums[i]
                curr_window.remove(nums[i])
                i+=1
            
            total += nums[j]
            curr_window.add(nums[j])
            

            if j-i+1 == k:
                # print(f"{i=} {j=}")
                max_sum = max(total, max_sum)
                total -= nums[i]
                curr_window.remove(nums[i])
                i+=1
            
            # print(f"{total=} {max_sum=}")
            j+= 1

        return max_sum
            