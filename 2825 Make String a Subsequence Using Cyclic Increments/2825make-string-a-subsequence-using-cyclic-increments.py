class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        
        m, n = len(str1),len(str2)

        if n > m:
            return False

        i, j = 0, 0
        
        while i < m and j < n:

            checked = False
            s1_char_num = ord(str1[i]) - ord('a')
            s2_char_num = ord(str2[j]) - ord('a')

            # print(f"{s1_char_num=} {s2_char_num=}")
            if s2_char_num == 0:
                if s1_char_num == 0 or s1_char_num == 25:
                    j+=1
                    checked = True


            if not checked and s2_char_num == s1_char_num  or s2_char_num == s1_char_num +1:
                j+=1
            
            if j == n:
                return True
            i+=1
        
        return False
                
