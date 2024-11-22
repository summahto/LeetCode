class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        patt_count = defaultdict(int)

        for i in range(m):
            # curr_arr = []
            start = matrix[i][0]
            s= ''
            for j in range(n):
                if matrix[i][j] == start:
                    s+='T'
                else:
                    s+='F'
                
            # s = ''.join(curr_arr)
            
            patt_count[s]+=1
        
        # print(f"{patt_count=}")

        return max(patt_count.values(), default=0)
            
