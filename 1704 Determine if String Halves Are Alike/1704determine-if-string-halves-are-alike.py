class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        uniq = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        i = 0
        j = len(s) -1
        lc, rc = 0, 0
        while i<j :
            if s[i] in uniq:
                lc+= 1

            if s[j] in uniq:
                rc+= 1

            i+= 1
            j-= 1

        
        return lc == rc

        