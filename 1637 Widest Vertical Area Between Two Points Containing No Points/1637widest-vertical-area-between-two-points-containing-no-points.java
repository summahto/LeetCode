class Solution {
    public int maxWidthOfVerticalArea(int[][] points) {
        
        Arrays.sort(points, (x, y) -> x[0] - y[0]);
        // System.out.println(Arrays.deepToString(points));

        int maxD = 0;

        for(int i=1 ;i< points.length; i++){
            maxD = Math.max(maxD, points[i][0] - points[i-1][0]);
        }


        return maxD;
    }
}