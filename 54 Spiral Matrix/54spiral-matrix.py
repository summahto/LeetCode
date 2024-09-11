class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        

        ans = []

        m = len(matrix)
        n = len(matrix[0])

        # matrix's row 
        top = 0
        bottom = m-1

        # matrix's columns
        l = 0
        r = n-1

        while top <= bottom and l <= r:

            dl = l
            while dl <= r and l<= r:
                ans.append(matrix[top][dl])
                dl += 1
            
            # print(ans)
            # top row parsing is done
            top += 1
            
            if top > bottom:
                break

            dt = top
            while dt <= bottom and top <= bottom:
                ans.append(matrix[dt][r])
                dt += 1
            

            # print(ans)
            # rightmost column is parsed
            r -= 1
            if l > r :
                break

            dr = r
            while dr >= l and l <= r:
                ans.append(matrix[bottom][dr])
                dr -= 1
            # print(ans)
            
            # bottom most row is parsed
            bottom -= 1
            db = bottom

            while db >= top and top <= bottom:
                ans.append(matrix[db][l])
                db -= 1
            # print(ans)
            
            # left most column is parsed
            l += 1
    
        return ans

