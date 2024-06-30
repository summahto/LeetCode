class Solution:
    def balancedString(self, s: str) -> int:
        l = 0
        r = 0
        
        c = Counter(s)
        exp = len(s)// 4

        # print(c)
        # print(exp)

        ans = 0
        min_len = n = len(s)

        while r < n:

            c[s[r]] -= 1
            
            while l< n and c['Q'] <= exp and c['W'] <= exp and c['E'] <= exp and c['R'] <= exp:
                min_len = min(min_len, r-l+ 1)
                c[s[l]] += 1
                l+= 1
            
            r += 1

        return min_len
