class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        
        maxLen = -1
        posMap = [-1] * 26

        for i in range(len(s)):
            idx = ord(s[i]) - ord('a')

            if posMap[idx] != -1:
                currLen = i - posMap[idx] - 1                
                maxLen = max(maxLen, currLen)

            else :
                posMap[idx] = i
                

        
        return maxLen
                