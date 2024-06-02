class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len (matrix[0])

        lo , hi = 0, (m * n)

        while lo < hi:
            mid = (lo + hi) // 2
            x_mid = mid // n
            y_mid = mid % n

            if matrix[x_mid][y_mid] < target:
                lo = mid + 1
            else :
                hi = mid

        # print(lo)

        if lo == (m*n) or matrix[lo//n][lo % n] != target:
            return False
        
        return True