class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        ans = []
        n = len(spaces)
        prev = 0
        for i in range(n):

            ans.append(s[prev: spaces[i]])
            prev = spaces[i]
        
        ans.append(s[prev:len(s)])

        return " ".join(ans)
