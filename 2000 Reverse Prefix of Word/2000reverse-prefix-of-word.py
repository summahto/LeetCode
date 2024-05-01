class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        def reverse(i, word):
            s = ""
            while i >= 0:
                s += word[i]
                i-= 1

            return s

        for i in range(len(word)):
            if word[i] == ch:
                # print(i)
                rev = reverse(i, word)
                # print(rev)
                return rev + word[i+1:len(word)]


        return word

        