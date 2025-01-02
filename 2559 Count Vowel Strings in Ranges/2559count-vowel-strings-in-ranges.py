class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:

        n = len(words)
        ans = []
        vowels = set(['a', 'e', 'i', 'o', 'u'])

        prefix = [0]*n
        for i in range(n):
            if words[i][0] in vowels and words[i][-1] in vowels:
                prefix[i] += 1

            if i > 0:
                prefix[i] += prefix[i-1]
        
        # print(prefix)

        for (l, r) in queries:
            if l == 0:
                ans.append(prefix[r])
            else:
                ansLR = prefix[r] - prefix[l-1]
                ans.append(ansLR)
            

        return ans
        