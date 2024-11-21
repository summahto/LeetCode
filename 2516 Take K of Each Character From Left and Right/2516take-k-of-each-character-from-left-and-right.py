from typing import List

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:

        n = len(s)
        
        all_chars = 'abc'
        char_freq = Counter(s)

        for char in all_chars:
            if char_freq[char] < k:
                return -1
        
        if k ==0 :
            return 0

        nd_max_len = 0

        i, j = 0, 0

        while j < n:
            
            char_freq[s[j]] -= 1

            while i <= j and (char_freq['a'] < k or char_freq['b'] < k or char_freq['c'] <k):
                char_freq[s[i]] += 1
                i+=1


            nd_max_len= max(j-i+1, nd_max_len)

            j+=1
        
        return n- nd_max_len
            
