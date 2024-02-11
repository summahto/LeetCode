class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def checkOddLenPal(i) :
            l = i-1
            r = i+1
            while(l >= 0 and r < len(s) and s[l] == s[r]) :
                l -= 1
                r += 1
            
            return r-l-1

        def checkEvenLenPal(l):
            r = l+1
            while(l >= 0 and r < len(s) and s[l] == s[r]) :
                l -= 1
                r += 1
            return r -l -1

        maxLen = 1
        st, e = 0,0
        for i in range(len(s)):
            
            currOddMax = checkOddLenPal(i)
            
            # print(currOddMax, maxLen)
            if currOddMax > maxLen :
                maxLen = currOddMax
                st = i - (maxLen//2)
                e = i + (maxLen//2)

            currEvenMax = checkEvenLenPal(i)
            # print(currEvenMax, maxLen)
            if currEvenMax > maxLen:
                maxLen = currEvenMax
                st = i - (maxLen -1)//2
                e = i + (maxLen//2)

        print(st, e)

        return s[st:e+1]   
            
            