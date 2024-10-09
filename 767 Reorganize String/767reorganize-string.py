class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)

        freq = Counter(s)
        freq = freq.most_common()
        # print(freq)

        # "aaab"
        # [('a', 3), ('b', 1)]

        maxFreq = freq[0][1]
        if maxFreq > (n+1)//2 :
            return ''

        ans = [''] * n

        i = 0
        for (char, f) in freq:
            for _ in range(f):
                if i >= n:
                    i = 1
                ans[i] = char

                i+= 2

        # print(ans)

        return ''.join(ans)


