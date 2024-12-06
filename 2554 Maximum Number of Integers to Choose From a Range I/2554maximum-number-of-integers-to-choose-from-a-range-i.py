class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        
        ban = set(banned)

        curr_sum = 0
        count = 0
        for i in range(1, n+1):
            if i in ban:
                continue
            
            curr_sum += i
            if curr_sum <= maxSum:
                count+=1
            else :
                break
        
        return count