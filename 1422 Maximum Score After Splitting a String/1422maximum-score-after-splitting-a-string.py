class Solution:
    def maxScore(self, s: str) -> int:
        
        c= Counter(s)
        ones = c['1']
        zeros = 0

        maxScore = float('-inf')

        for i in range(len(s) -1):
            
            if s[i] == '1':
                ones-=1
            else:
                zeros += 1
            
            score = ones + zeros
            maxScore = max(score, maxScore)

        return maxScore

            

