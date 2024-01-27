class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        @lru_cache(None)
        def dfs(i, j, moves):
            
            # add 1 to the total paths if you breach the boundary
            if (i == -1 ) or (j == -1 ) or (i == m) or (j == n):
                return 1

            # if you are anywhere in the matrix but have no moves left return 0
            if moves == 0:
                return 0
            
            
            return  (dfs(i+1, j, moves -1) + 
                    dfs(i-1, j, moves -1) +
                    dfs(i, j+1, moves -1) +
                    dfs(i, j-1, moves -1))

        return dfs(startRow, startColumn, maxMove) % (10**9 +7)