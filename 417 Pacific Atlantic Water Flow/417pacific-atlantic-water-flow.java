class Solution {
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        
        if(heights.length == 0)
            return null;
        
        List<List<Integer>> result = new ArrayList<>();
        
        if(heights.length == 1 && heights[0].length == 1){
            result.add(new ArrayList<>(Arrays.asList(0, 0)));
            return result;
        }

        int m = heights.length , n = heights[0].length;

        boolean [][] pacific = new boolean[m][n];
        boolean [][] atlantic = new boolean[m][n];

        for(int j=0; j< n; j++){
            dfs(heights, 0, j, Integer.MIN_VALUE, pacific);
            dfs(heights, m-1, j, Integer.MIN_VALUE, atlantic);
        }

        for(int i=0; i< m; i++){
            dfs(heights, i, 0, Integer.MIN_VALUE, pacific);
            dfs(heights, i, n-1, Integer.MIN_VALUE, atlantic);
        }

        for(int i =0 ; i< m; i++){
            for(int j=0; j< n; j++){
                if(pacific[i][j] && atlantic[i][j])
                    result.add(List.of(i,j));
            }
        }

        

        return result;
        
    }

    int [][] dir = new int [][]{ {0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    public void dfs(int [][] heights, int i, int j, int prev, boolean[][] visited){
        
        int m = heights.length, n= heights[0].length;

        if(i < 0 || i>= m || j<0 || j>= n ) 
            return;
        
        if(visited[i][j] || heights[i][j] < prev)
            return;
        
        visited[i][j] = true;
        for (int [] d : dir){
            dfs(heights, i+ d[0], j+d[1], heights[i][j], visited);
        }

    }

}