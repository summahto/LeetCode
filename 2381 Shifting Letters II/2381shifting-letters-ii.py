class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)

        diff = [0] * n

        for start, end, d in shifts:

            if d == 1:
                diff[start] += 1
                
                if end + 1 < n:
                    diff[end + 1] -=1 
            
            else:
                diff[start] -= 1
                if end +1 < n:
                    diff[end + 1] += 1
        
        ans = list(s)

        # print(ans)
        currShift = 0
        for i in range(n):

            currShift+= diff[i]

            # get the ordinal value of current char : `ord(ans[i]) - ord('a')`
            # add the shift : `currShift`
            # get the position of new char in 26 letters : `%26`
            # add the ordinal value of 'a' : 97 : to get the ascii value of new char
            shiftedChar = chr (((ord(ans[i]) - ord('a') + currShift) % 26) + ord('a'))
            ans[i] = shiftedChar


        return ''.join(ans)
