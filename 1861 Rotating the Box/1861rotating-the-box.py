class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        
        m = len(box)
        n = len(box[0])

        # parse from the last column onwards and shift all the obstacles to the rightmost position possible

        for j in range(n-1, -1, -1):

            for i in range(m):

                if box[i][j] == '#':
                    curr_row = i
                    # start moving the stone right until there is an obsatcle or end
                    box[i][j] = '.'

                    k = j+1
                    while k < n and box[i][k] == '.':
                        k+= 1
                    
                    box[i][k-1] = '#'
        
        ans = [[0]* m for _ in range(n)]
        # print(ans)

        for i in range(m):
            for j in range(n):
                ans[j][m-i-1]= box[i][j]

        
        return ans                            

