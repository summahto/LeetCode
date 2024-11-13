class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        
        n = len(nums)

        sorted_nums = sorted(nums)
        
        count = 0
        for i in range(len(sorted_nums)):
            lp = lower - sorted_nums[i]
            up = upper - sorted_nums[i]

            left_index = bisect_left(sorted_nums, lp, lo=i+1)
            right_index = bisect_right(sorted_nums, up, lo= i+1)
            # print(f"{left_index=} {right_index=}")

            count += right_index - left_index

            # for i in range(left_index, right_index):
            #     if num_index_map[sorted_nums[i]] > num_index_map[num]:
            #         count += 1
            #         print(f"{num} {sorted_nums[i]}")
        
        
        return count