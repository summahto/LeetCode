class Solution:
    def makeFancyString(self, s: str) -> str:
        
        if len(s) <= 2:
            return s
            
        ans = []

        ans.append(s[0])
        ans.append(s[1])
        # 0 1 2 3 4 5 6 7 8
        # l e e e t c o d e
        for i in range(2, len(s)):    
            if s[i] == s[i-1] and s[i] == s[i-2]:
                continue
            
            ans.append(s[i])
            
        return ''.join(ans)
            

            