class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        
        n = len(code)
        ans = [0]*n
        if n == 1:
            return [0] #check this
        
        if k == 0:
            return ans

        elif k > 0:
            i = 0

            while i < n:
                j = i+1
                total = 0

                while j-i <= k:
                    total += code[j%n]
                    j+=1
                
                ans[i]= total
                i+=1

        else:
            i= n-1

            while i >=0 :
                j = i-1
                total = 0

                while j - i >= k:
                    # print(j % n)   
                    total += code[j%n]
                    j-=1
                
                ans[i] = total
                i-=1
            
        return ans
        

        
