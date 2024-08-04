class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        
        n = len(nums)

        # ctr = Counter(nums)
        
        totalOnes = sum(nums)

        if totalOnes == 0 or totalOnes == 1:
            return 0

        currOnes = 0
        maxOnes = 0

        # Since the array is circular
        # To cover the window which starts from the end and finishes at the start
        # we are starting j = 1
        # [1,1,0,0,1]
        # starting window : i = -2 and j = 1
        j = 1
        i = j - totalOnes # i = -2
        j = i # j = -2

        minSwaps = float('inf')

        while j < n:
            
            if nums[j] == 1:
                currOnes += 1

            if j-i+1 > totalOnes:
                if nums[i] == 1:
                    currOnes -= 1
                i+=1
                
            maxOnes = max(currOnes, maxOnes)

            j+= 1

        return totalOnes - maxOnes
  