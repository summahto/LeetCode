class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # Intuition:
        # most important in this problem, all the numbers are a sustring of the all string
        all = "123456789"
        res = []
        minLen = len(str(low))
        maxLen = len(str(high))
        
        for window in range(minLen, maxLen + 1):

            i = 0
            j = i+ window

            # since you are not accessing the jth index and just getting the substring you don't have to go 
            # till len-1, you can go till j = len
            while j <= len(all) :
                curr = int(all[i:j])
                # optimized this : initial idea was to increment i and j before continue and after appending
                i+=1
                j+=1

                if curr < low :
                    continue
            
                if curr > high :
                    break
        
                res.append(curr)

        return res
        
