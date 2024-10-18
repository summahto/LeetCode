class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, maxLen = 0, 0, 0
        uniq = set()

        while r < len(s):

            while s[r] in uniq:
                # remove all the elements until that char at r
                uniq.remove(s[l])
                l += 1
        
            uniq.add(s[r])
            maxLen = max(maxLen, r-l +1)
            r+=1
        
        return maxLen
