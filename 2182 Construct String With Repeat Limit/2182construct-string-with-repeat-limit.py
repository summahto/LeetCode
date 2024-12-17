class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        
        freq = [0] *26

        for c in s:
            freq[ord(c) - ord('a')]+= 1
        
        # first = 25
        i = 25
        ans = []
        while i >= 0:
            charsAvailable = False

            # need two chars to alternate between them
            while i >= 0 and freq[i] == 0:
                i -= 1

            if freq[i] > repeatLimit:
                # put repeatLimit number of chars in the ans and then add the next available char
                charsAvailable = True
                for _ in range(repeatLimit):
                    ans.append(chr(97+i))
                
                freq[i] -= repeatLimit
            else:
                for z in range(freq[i]):
                    ans.append(chr(97+ i))
                freq[i] = 0

            if charsAvailable:
                j = i-1
                
                # two condition which satisfy onlt then we enter the loop
                while j >= 0 and freq[j] == 0:
                    j-=1
                    
                # either of the above condition can fail
                # if j git decremented until it was less than 0
                if j < 0:
                    break
                
                # Now got a valid j and freq[j] != 0, which means > 0
                ans.append(chr(97+j))
                freq[j] -= 1
        
        return "".join(ans)
