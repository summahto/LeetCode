class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        n = len(heights)
        heightCount = [0]*101
        result = 0

        for h in heights:
            heightCount[h]+=1

        currH = 0 # parse through all the indexes of heightCount which represent the height
        for i in range(n):
            while heightCount[currH] == 0:
                currH+=1
            
            if heights[i] == currH:
                heightCount[currH] -= 1

            else:
                result +=1
                heightCount[currH] -= 1
                # even if it is not equal we will still decrement because that comparison is done once.

        return result

