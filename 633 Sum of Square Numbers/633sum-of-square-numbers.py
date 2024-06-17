class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        

        if c == 0 or c == 1 or c == 2:
            return True

        n = c**(1/2)
        i = 0
        compSet = set() 

        while i<= n:
            
            if (i**2) == c/2:
                return True
            
            if (i**2) in compSet:
                return True

            compSet.add(c - (i**2))
            i+=1


        return False