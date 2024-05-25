class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        if len(nums) == 0:
            return []
        
        if len(nums) == 1:
            return [f"{nums[0]}"]

        ans = []
        i = 1
        l, r = 0, 0
        while i< len(nums):
            if nums[i] - nums[i-1] > 1:
                # this is the last number of the seq
                if l == r:
                    ans.append(f"{nums[l]}")
                else :
                    ans.append(f"{nums[l]}->{nums[r]}")
                    l = r

                l+=1
                r+=1
                            
            else :
                # keep going forward
                r+=1
            
            i+=1
        
        # adding the last range pair left
        if l == r:
            ans.append(f"{nums[l]}")
        else :
            ans.append(f"{nums[l]}->{nums[r]}")


        return ans
