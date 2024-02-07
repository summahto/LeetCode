class Solution:
    def frequencySort(self, s: str) -> str:
        
        c = Counter(s)

        sortedTuple = sorted(c.items(), key=lambda item:item[1], reverse=True)

        freqList = []
        for item in sortedTuple:
            for i in range(item[1]):
                freqList.append(item[0])
        
        ans = "".join(freqList)

        return ans
        