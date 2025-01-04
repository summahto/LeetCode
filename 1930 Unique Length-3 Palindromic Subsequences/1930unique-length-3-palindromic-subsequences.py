class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        fr = Counter(s)
        fl = Counter()

        fr[s[0]] -= 1
        # fr[s[1]] -= 1
        fl[s[0]] += 1
        count = 0
        uniq = set()
        
        if fr[s[0]] == 0:
            del[fr[s[0]]]
        

        for i in range(1, len(s) -1):
            fr[s[i]] -= 1
            
            if fr[s[i]] == 0:
                del fr[s[i]]

            # print(f"{fl=} {fr=}")
            for key in fl:
                if key in fr:
                   uniq.add(key + s[i] + key) 

            fl[s[i]] +=1

            if fl[s[i]] == 0:
                del fl[s[i]]
        
        # print(uniq)
        return len(uniq)