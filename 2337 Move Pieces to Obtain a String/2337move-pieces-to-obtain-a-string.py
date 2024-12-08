class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # Letters cannot cross each other, so the ith letter in start should be the same as ith letter in target
        n = len(start)
        i, j = 0, 0

        # Or is required for the following case: 
        # start = "_L"
        # end =   "LR"
        while i < n or j< n:

            while i < n and start[i] == '_':
                i += 1
            
            while j < n and target[j] == '_':
                j += 1
            
            if i == n and j == n:
                return True
            
            # if i reaches to the end before j or vice versa, that means there was at least 1 char missing
            # for this case to come into picture we need the "OR" condition for the while loop
            if i == n or j == n:
                return False
            
            if start[i] != target[j] :
                return False
            else :
                if (start[i] == 'L' and j >i)  or (start[i] == 'R' and j < i):
                    return False
            
            i+=1
            j+=1
        
        return True

