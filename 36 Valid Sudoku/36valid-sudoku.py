class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        unique = set()

        for i in range (len(board)):

            for j in range (len(board[i])):

                if board[i][j] != ".":

                    if (board[i][j] + "r" + str(i) in unique) or (board[i][j] + "c" + str(j) in unique) or (board[i][j] + str(i//3) + str(j//3) in unique): 
                        return False

                    unique.add(board[i][j] + "r" + str(i))
                    unique.add(board[i][j] + "c" + str(j))
                    unique.add(board[i][j] + str(i//3) + str(j//3))

        
        return True