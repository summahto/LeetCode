class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        ans = []

        maxFreq = Counter()

        for w in words2:
            c1 = Counter(w)

            for c, f in c1.items():
                if f > maxFreq[c]:
                    maxFreq[c] = f
        
        # print(maxFreq)

        for word in words1:
            wc = Counter(word)

            for c, f in maxFreq.items():
                if wc[c] < f:
                    break
            else :
                ans.append(word)

        return ans
            