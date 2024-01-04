class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        freqMap = defaultdict(int)

        for n in nums:
            freqMap[n] +=1
        
        ops = 0
        for key, value in freqMap.items():
            if value < 2:
                return -1

            while value > 0:

                if value % 3 == 0:
                    ops += (value // 3)
                    value = 0
                    
                else :
                    ops += 1
                    value -= 2
            
                
        
        return ops