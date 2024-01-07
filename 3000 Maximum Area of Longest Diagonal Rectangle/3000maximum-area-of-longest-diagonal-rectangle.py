class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        
        n = len(dimensions)
        maxDiag = 0
        maxArea = 0
        for i in range(n):
            
            currDiag = math.sqrt(dimensions[i][0]* dimensions[i][0] + dimensions[i][1] * dimensions[i][1])
            if currDiag > maxDiag :
                maxDiag = currDiag
                # maxDim = dimensions[i]
                maxArea = dimensions[i][0] * dimensions[i][1]
                
                
            elif currDiag == maxDiag:
                maxArea = max(maxArea, dimensions[i][0] * dimensions[i][1])
                
        
        
        return maxArea