class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        gMax, lMax = 0,1 
        unique = set()
        for i in range(len(nums)):
            unique.add(nums[i])

        for i in range (len(nums)):
            lMax = 1
            if (nums[i]+1) in unique:
                pass
            
            else:
                val = nums[i]
                while (val -1) in unique:
                    lMax += 1
                    val -= 1
                    # print(val , lMax)

                gMax = max(gMax, lMax)

        return gMax

                     