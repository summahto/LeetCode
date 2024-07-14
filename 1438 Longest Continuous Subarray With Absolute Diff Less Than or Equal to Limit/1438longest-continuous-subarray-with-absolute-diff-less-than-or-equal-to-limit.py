from sortedcontainers import SortedDict

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        window = SortedDict()

        l = r = 0
        n = len(nums)
        ans = 0
        while r < n:
            # maintain the counter of each element
            if nums[r] in window:
                window[nums[r]] += 1
            else :
                window[nums[r]] = 1

            # check if last - first is within the limit
            while window.peekitem(-1)[0] - window.peekitem(0)[0] > limit:
                
                # if not, then reduce the count of the left element
                window[nums[l]] -= 1

                if window[nums[l]] == 0:
                    del window[nums[l]]

                l += 1

            ans = max(ans, r -l +1)

            r+=1 

        
        return ans
        

