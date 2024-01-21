class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        n = len(arr)
        sum = 0

        stack = []
        for i in range(n):
            
            currMultiplier = 1
            while stack and arr[i] < stack[-1][0]:
                val, idx, multiple = stack.pop()
                sum += val* (i - idx) * multiple
                currMultiplier += multiple

            
            stack.append((arr[i], i, currMultiplier))
        
        i+= 1

        while stack :
            val, idx, multiple = stack.pop()
            sum += val* (i - idx) * multiple
        
            
        return sum % (10**9 +7)