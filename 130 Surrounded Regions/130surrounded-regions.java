class Solution {
    public void solve(char[][] board) {

        int m = board.length , n= board[0].length;
        // boolean [][] visited = new boolean[m][n];
        // boolean [][] notSurr = new boolean[m][n];

        for(int j=0; j<n; j++){
            if(board[0][j] == 'O')
                dfs(board, 0, j, m, n);
            if(board[m-1][j] == 'O')
                dfs(board, m-1, j, m ,n);
        }

        for(int i =0; i< m; i++){
            if(board[i][0] == 'O')
                dfs(board, i, 0, m, n);
            if(board[i][n-1] == 'O')
                dfs(board, i, n-1, m, n);
        }

        for(int i =0 ; i<m ;i++){
            for(int j = 0; j< n; j++){
                if(board[i][j] == 'O') board[i][j] = 'X';
                if(board[i][j] == 'T') board[i][j] = 'O';
            }
        }
    }

    int [][] dirs = {{1,0}, {0,1}, {0,-1}, {-1, 0}};
    public void dfs(char [][] board, int i, int j, int m, int n){

        if(i < 0 || i >= m || j< 0 || j>= n || board[i][j] != 'O')
            return;
        
        if(board[i][j] == 'O')
            board[i][j] = 'T' ;        

        for(int [] dir : dirs){
            dfs(board, i+dir[0], j+dir[1], m, n);
        }
        
        
    }
}