class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        i, j = 0 , 0
        count = 0
        
        while i < len(t) and j < len(s):
            if t[i] == s[j]:
                i+=1
                j+=1
            else :
                j+=1

        count += len(t) -i 
        return count