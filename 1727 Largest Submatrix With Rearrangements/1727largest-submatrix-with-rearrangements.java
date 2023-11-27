class Solution {
    public int largestSubmatrix(int[][] matrix) {
        
        int area = 0, maxSoFar = 0;
        int m = matrix.length;
        int n = matrix[0].length;
        int [] heights = matrix[0];

        for(int i= 0; i< matrix.length; i++){
            if(i > 0){
                
                for(int j = 0; j< matrix[i].length; j++){
                    
                    if(matrix[i][j] == 1)
                        heights[j] += matrix[i][j];
                    else 
                        heights[j] = 0;

                    
                }
                
            }
            
            // create a copy and then sort it, otherwise the heights array will change and cause issues in the 2nd iteration
            int clone [] = heights.clone();
            Arrays.sort(clone);
            // System.out.println(Arrays.toString(clone));

            for (int k = n -1; k >= 0; k--) {
                maxSoFar = Math.max(maxSoFar, clone[k] * (n - k));
            }

            // area = largestRectangleArea(heights);

        }

        return maxSoFar;
    }
}