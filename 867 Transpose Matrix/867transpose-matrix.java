class Solution {
    public int[][] transpose(int[][] matrix) {
        int m = matrix.length;
        int [][] ans = new int [matrix[0].length][m];
        
        for(int i=0; i< m ;i++){

            int n = matrix[i].length;
            for(int j=0 ;j < n; j++){

                ans[j][i] = matrix[i][j];
            }

        }

        return ans;
    }
}