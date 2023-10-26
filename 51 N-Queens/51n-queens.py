class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        

        board = [['.'] * n for i in range(n)]
        col = set()
        posDiag = set()
        negDiag = set()
        res = list()

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c not in col and (r+c) not in posDiag and (r-c) not in negDiag:
                    board[r][c] = 'Q'
                    
                    col.add(c)
                    posDiag.add(r+c)
                    negDiag.add(r-c)

                    backtrack(r+1)

                    board[r][c] = '.'
                    col.remove(c)
                    posDiag.remove(r+c)
                    negDiag.remove(r-c)


        backtrack(0)    

        return res
        


        