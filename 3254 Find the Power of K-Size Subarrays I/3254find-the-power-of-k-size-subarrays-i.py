class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:

        if k == 1:
            return nums
        
        n = len(nums)
        ans = []

        i, j = 0, 1
        count = 1
        
        while j < n:

            if nums[j] - nums[j-1] == 1:
                count += 1
            # else:
            #     count -= 1
            
            if j-i+1 == k:
                # print(f"{count=}")

                if count == k:
                    ans.append(nums[j])
                else:
                    ans.append(-1)
                
                if nums[i+1] - nums[i] == 1:
                    count-= 1

                i+=1

            j+= 1

        return ans


