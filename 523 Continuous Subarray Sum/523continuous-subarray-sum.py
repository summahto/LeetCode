class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        rem_map = {0 : -1}
        sum = 0
        
        i = 0 
        while i< n:
            sum += nums[i]
            rem = sum %k

            if rem in rem_map:
                if i - rem_map[rem] > 1:
                    return True
            else :
                rem_map[rem] = i    
            i+=1    


        return False

