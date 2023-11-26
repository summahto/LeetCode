class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = [] # will contain pair heights and their posistion
        area, maxSoFar = 0, 0

        for i in range(len(heights)) :
            startIndex = i
            while(stack and heights[i] < stack[-1][0]):
                
                prevHeight, index = stack.pop()
                area = prevHeight*(i - index)
                maxSoFar = max(maxSoFar, area)
                startIndex = index
            

            stack.append((heights[i], startIndex))
        
        # print(i)

        while(stack):
            prevHeight, index = stack.pop()
            # print(prevHeight, index, i)
            area = prevHeight*((i+1) - index)
            maxSoFar = max(maxSoFar, area)
        
        return maxSoFar
        
            
