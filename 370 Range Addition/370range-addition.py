class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        
        ans = [0] * length
        diff = [0] * length
        
        for start, end, val in updates:
            diff[start] += val
            
            if end + 1 < length:
                diff[end + 1] -= val
            
        
        currUpdate = 0

        for i in range(length):
            currUpdate += diff[i]
            ans[i] = currUpdate

        return ans
        
