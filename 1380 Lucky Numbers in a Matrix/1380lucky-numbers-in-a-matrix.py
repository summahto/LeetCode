class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        row_min = []

        for i in range(m):
            row_min.append(min(matrix[i]))

        print(row_min)

        col_max = []

        for j in range(n):
            cMax = float('-inf')

            for i in range(m):
                cMax = max(cMax, matrix[i][j])
            
            col_max.append(cMax)


        ans = []
        for i in range(m):

            for j in range(n):

                if row_min[i] == col_max[j]:
                    ans.append(row_min[i])

        

        return ans
