class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        char_map = {}
        j = 1
        for i in range(97, 123):
            char_map[chr(i)] = j
            j+= 1
        
        # print(char_map)
        
        ans = ''
        for i in range(len(s)):
            ans += str(char_map[s[i]])


        num = int(ans)

        # print(num)

        sum = 0
        while k > 0:

            sum = 0
            while num > 0:
                sum += num % 10
                num = num//10
            
            # print(sum, num)
            k -= 1
            num = sum

        return sum