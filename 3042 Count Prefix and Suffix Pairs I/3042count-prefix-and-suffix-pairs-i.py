class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        count = 0

        for i in range(n-1):

            for j in range(i+1, n):
                if len(words[j]) <  len(words[i]):
                    continue

                count += words[j].startswith(words[i]) and words[j].endswith(words[i])
                    

        return count