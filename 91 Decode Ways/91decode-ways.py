class Solution:
    def numDecodings(self, s: str) -> int:
        
        invalid_chars = set(["00", "30", "40", "50", "60", "70", "80", "90"])
        contains_invalid = any(st in s for st in invalid_chars)

        if(s.startswith('0') or contains_invalid):
            return 0

        n = len(s)
        dp = [0] * (n+1) 

        dp[0] =1 
        
        # Actually we don't need this because we are already checking it on the top
        if s[0] != '0':
            dp[1] = 1

        
        for i in range(2, n+1):
            
            single = int(s[i-1])

            if single > 0 and single < 10:
                dp[i] += dp[i-1]
            
            double = int(s[i-2:i])

            if double > 9 and double < 27:
                dp[i] += dp[i-2]

    

        return dp[n]            
        

    