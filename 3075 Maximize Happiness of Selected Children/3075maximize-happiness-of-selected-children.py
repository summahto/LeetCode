class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        
        n = len(happiness)
        happiness.sort()
        dec = 0
        sum = 0
        i = n-1
        while i >= 0:
            if k > 0 and (happiness[i] - dec) > 0:
                sum += (happiness[i] - dec)
                dec += 1
                k-=1
            else :
                break
            
            i-= 1

                
        return sum