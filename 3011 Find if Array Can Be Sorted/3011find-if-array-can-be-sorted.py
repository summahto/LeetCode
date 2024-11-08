class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        
        n = len(nums)
        prev = None
        # [8,4,2,30,15]
        # 3,5, 16,8,4,2
        #       i        
        # prev : last island - bit_count, min, max
        prev_max = float('-inf')
        curr_bit_count = nums[0].bit_count()
        curr_max = nums[0]
        curr_min = nums[0] 
        
        for i in range(1, n):
            
            if nums[i].bit_count() == curr_bit_count:
                # new element is part of the same curr group
                curr_max = max(curr_max, nums[i])
                curr_min = min(curr_min, nums[i])
            else:
                if curr_min < prev_max:
                    return False
                # set the max/min of new elements
                prev_max = curr_max
                curr_max = nums[i]
                curr_min = nums[i]
                curr_bit_count = nums[i].bit_count()

        if curr_min < prev_max:
            return False

        return True