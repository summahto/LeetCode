class Solution:
    def totalNQueens(self, n: int) -> int:
    
        col = set()
        posDiag = set()
        negDiag = set()
        ans = 0

        def backtrack(r):
            
            if r == n:
                nonlocal ans
                ans += 1
                return
                

            for c in range(n):
                if c not in col and (r+c) not in posDiag and (r-c) not in negDiag:
                    # choose
                    col.add(c)
                    posDiag.add(r+c)
                    negDiag.add(r-c)


                    # recurse
                    backtrack(r+1)

                    # backtrack
                    # after all the combinations in the column have been tried 
                    # comes back to previous recursive call. Now remove this and try next pos
                    
                    col.remove(c)
                    posDiag.remove(r+c)
                    negDiag.remove(r-c)

        backtrack(0)
        return ans
                