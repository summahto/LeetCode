class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m = len(board)
        n = len(board[0])
        # i -> row
        # j -> column
        # k -> index of word
        board2 = deepcopy(board)

        def dfs(i, j, k):

            if k == len(word):
                return True

            if i < 0 or i == m or j < 0 or j == n or board[i][j] != word[k]:
                return False
            
            # visited[i][j] = True

            ans = False
            if board[i][j] == word[k] :
                board[i][j] = "."
                ans = dfs(i+1, j, k+1) or dfs(i-1, j, k+1) or dfs(i, j+1, k+1) or dfs(i, j-1, k+1)
                # visited[i][j] = False
            
            # visited[i][j] = False

            board[i][j] = board2[i][j]

            return ans
            
        res = False
        for i in range(m):

            for j in range(n):
                # visited = [[False for x in range(n)] for _ in range(m)]

                if board[i][j] == word[0] :
                    # visited[i][j] = True
                    board[i][j] = "."
                    res = dfs(i+1, j, 1) or dfs(i-1, j, 1) or dfs(i, j+1, 1) or dfs(i, j-1, 1)
                    
                    if res:
                        return res
                    board[i][j] = board2[i][j]

        return False


        