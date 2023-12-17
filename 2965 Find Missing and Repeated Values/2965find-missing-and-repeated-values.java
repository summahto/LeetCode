class Solution {
    public int[] findMissingAndRepeatedValues(int[][] grid) {
        
        int [] ans = new int[2];
        int n = grid.length;
        Set<Integer> uniq = new HashSet<>();
        Set<Integer> all = new HashSet<>();
        int total = 0;
        
        for(int i = 1; i<= n*n; i++){
            all.add(i);
            total += i;
        }
        
        // System.out.println(total);
        
        for(int i=0; i< n ;i++){
            
            for(int j=0; j<n ; j++){
                
                if(!uniq.add(grid[i][j]))
                    ans[0] = grid[i][j];
                else 
                    total -= grid[i][j];
                
            }
        }
        // System.out.println(total);
        ans[1] = total;
        
        return ans;
    }
}