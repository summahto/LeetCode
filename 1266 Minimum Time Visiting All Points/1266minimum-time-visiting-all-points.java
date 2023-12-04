class Solution {
    public int minTimeToVisitAllPoints(int[][] points) {
        
        int seconds = 0;
        int [] prev = points[0];
        int i =1;
        
        while(i< points.length){
            int [] curr = points[i];
            seconds += Math.max(Math.abs(curr[0] - prev[0]), Math.abs(curr[1]- prev[1]));
            prev = curr;
            i++;
        }

        // seconds++;

        // prev = curr;
        // continue;

        return seconds;
    }
}