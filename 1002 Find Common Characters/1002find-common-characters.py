class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        res = Counter(words[0])
        i = 1

        while i < len(words):
            res = res & Counter(words[i])
            i+=1
        

        return list(res.elements())