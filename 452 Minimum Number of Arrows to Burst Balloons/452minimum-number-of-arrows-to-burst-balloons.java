class Solution {
    public int findMinArrowShots(int[][] points) {
        if(points == null || points.length == 0)
            return 0;

        Arrays.sort(points, (p1, p2) -> Integer.compare(p1[0], p2[0]));
        int endPoint = points[0][1];
        int count = 1;
        for(int i =1; i< points.length ; i++){
            //start point of next array is less than current end point, do not increment endpoint
            if(points[i][0] <= endPoint){

                endPoint = Math.min(endPoint, points[i][1]);
            } else { //otherwise we need a new arrow and now the end point is the updates one
                count++;
                endPoint = points[i][1];
            }
        }

        return count;
        
    }
}