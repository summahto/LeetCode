class Solution {
    public int orangesRotting(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        Queue<Pair<Integer, Integer>> q= new LinkedList<>();

        for(int i=0 ; i< m; i++){

            for (int j=0; j< n;j++) {
                
                if(grid[i][j] == 2)
                    q.add(new Pair<>(i, j));
            }
        }

        int min = 0;
        while(!q.isEmpty()){

            int size = q.size();

            boolean isOrangeChanged = false;
            for(int i = 0; i< size; i++){
                
                Pair <Integer, Integer> p = q.remove();
                int x = p.getKey();
                int y = p.getValue();

                if(x+1 < m && grid[x+1][y] == 1){
                    q.add(new Pair<>(x+1, y));
                    grid[x+1][y] = 2;
                    isOrangeChanged = true;
                }

                if(y+1 < n && grid[x][y+1] == 1){
                    q.add(new Pair<>(x, y+1));
                    grid[x][y+1] = 2;
                    isOrangeChanged = true;
                }

                if(x-1 >= 0 && grid[x-1][y] == 1){
                    q.add(new Pair<>(x-1, y));
                    grid[x-1][y] = 2;
                    isOrangeChanged = true;
                }

                if(y-1 >= 0 && grid[x][y-1] == 1){
                    q.add(new Pair<>(x, y-1));
                    grid[x][y-1] = 2;
                    isOrangeChanged = true;
                }
            }

            if(isOrangeChanged)
                min++;
            
        }

        for(int i=0 ; i< m; i++){

            for (int j=0; j< n;j++) {
                
                if(grid[i][j] == 1)
                   return -1;
            }
        }

        return min;   
    }

}