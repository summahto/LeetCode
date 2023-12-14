class Solution {
    public int[][] onesMinusZeros(int[][] grid) {
        
        int m = grid.length, n = grid[0].length;

        int [] row1Count = new int[m];
        int [] row0Count = new int[m];
        int [] col1Count = new int[n];
        int [] col0Count = new int[n];

        for(int i= 0; i < m ; i++){

            for(int j=0; j< n; j++){

                if(grid[i][j] == 1){
                    row1Count[i]++;
                    col1Count[j]++;

                } else {
                    row0Count[i]++;
                    col0Count[j]++;

                }

            }
        }

        int [][] diff = new int[m][n];

        for(int i=0; i< m; i++){
            for(int j=0; j<n; j++){

                diff[i][j] = row1Count[i] + col1Count[j] - row0Count[i] - col0Count[j];
            }
        }

        return diff;


    }
}