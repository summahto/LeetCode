class Solution:
    def countSeniors(self, details: List[str]) -> int:
        
        i = 0
        n = len(details)
        ans = 0
        while i < n:
            age = int(details[i][11:13])
            if age > 60:
                ans += 1
                # print(age)
            
            i +=1
        
        return ans


        