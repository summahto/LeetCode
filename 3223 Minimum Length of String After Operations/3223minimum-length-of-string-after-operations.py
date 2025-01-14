class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)

        freq = Counter(s)
        ans =0
        for c, f in freq.items():

            if f%2 ==1:
                ans+= 1
            else:
                ans += 2

        
        return ans

