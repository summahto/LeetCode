class Solution {
    public int[][] imageSmoother(int[][] img) {
        
        int m = img.length, n = img[0].length;
        int ans [][] = new int [m][n];

        for(int i =0 ; i< m ; i++){

            for(int j = 0; j< n; j++){

                ans[i][j]= smoothen(i, j, img);
            }
        }


        return ans;
    }

    private int smoothen(int i, int j, int[][] img) {
        int [][] neighbours = {{-1, -1}, {-1, 0}, {-1, 1},
                {0, -1}, {0, 0}, {0, 1},
                {1, -1}, {1, 0},  {1, 1}};
        int count = 0, sum = 0;
        int m = img.length, n = img[0].length;

        for(int k = 0; k< neighbours.length; k++){

            int x = i + neighbours[k][0];
            int y = j + neighbours[k][1];

            if(( x >= 0) && (x < m) && ( y >= 0) && (y < n) ){
                sum += img[x][y];
                // System.out.print((x) + "," + (y) + " : ");
                count++ ;
            }
        }

        // System.out.print(sum + " : ");
        // if(sum > 0)
        //     sum /= count;
        // System.out.print(count + " : " + sum);
        // System.out.println();

        return sum/count;
    }
}