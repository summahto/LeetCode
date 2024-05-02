class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        
        uniq = set()
        max_num = -1
        for num in nums:
            if -num in uniq:
                max_num = max(abs(num), max_num)
            else :
                uniq.add(num)

        return max_num